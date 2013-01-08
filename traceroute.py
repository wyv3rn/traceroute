#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
traceroute - Get traceroute results with associated geolocation information
for each hop for a specified host from geographically distant source(s).
"""

__author__ = 'Dazzlepod (info@dazzlepod.com)'
__copyright__ = 'Copyright (c) 2013 Dazzlepod'
__version__ = '$Revision: #7 $'

import datetime
import json
import optparse
import os
import re
import sys
import urllib
import urllib2
from multiprocessing import Process
from subprocess import Popen, PIPE


class Traceroute(object):
    """Traceroute instance."""
    def __init__(self, ip_address='8.8.8.8', debug=False):
        super(Traceroute, self).__init__()
        self.ip_address = ip_address
        self.debug = debug
        # cache geocoded IP addresses during the lifetime of this instance
        self.locations = {}

    def traceroute(self):
        """Instead of running the actual traceroute command, we will fetch
        standard traceroute results from several publicly available webpages
        that are listed at traceroute.org.

        For each hop, we will then attach geolocation information to it."""
        self.print_debug("ip_address = %s" % self.ip_address)
        if not os.path.exists('%s.txt' % self.ip_address):
            (status_code, traceroute) = self.get_traceroute_output()
            f = open('%s.txt' % self.ip_address, 'w')
            f.write(traceroute)
            f.close()

        traceroute = open('%s.txt' % self.ip_address, 'r').read()

        # hops = dicts with keys: hop_num, hosts
        hops = self.get_hops(traceroute)

        # hops = dicts with keys: hop_num, hostname, ip_address, rtt
        hops = self.get_formatted_hops(hops)

        # hops = dicts with keys: hop_num, hostname, ip_address, rtt, location
        hops = self.get_geocoded_hops(hops)

        # hops = dicts with keys: hop_num, ip_address, latitude, longitude, rtt
        hops = self.get_stripped_hops(hops)

        return hops

    def get_traceroute_output(self):
        """Fetch traceroute output from a webpage."""

        # Example from traceroute.org
        url = "http://www.net.princeton.edu/cgi-bin/traceroute.pl"
        (status_code, response) = self.urlopen(url, context = {'target': self.ip_address})

        pattern = re.compile(r'<pre.*?>(?P<traceroute>.*?)</pre>', re.DOTALL|re.IGNORECASE)
        traceroute = re.findall(pattern, response)[0].strip()

        return (status_code, traceroute)

    def get_hops(self, traceroute):
        """Get hops from a traceroute output and return the hops in an array
        of dicts each representing hop number and the associated hosts data."""
        hops = []

        lines = traceroute.split('\n')
        for line in lines:
            line = line.strip()
            hop = {}
            if not line: continue
            try:
                hop = re.match(r'^(?P<hop_num>\d+)(?P<hosts>.*?)$', line).groupdict()
            except AttributeError:
                continue
            self.print_debug(hop)
            hops.append(hop)

        return hops

    def get_formatted_hops(self, hops):
        """hosts data from get_hops() is represented in a single string.
        We use this function to better represent the hosts data in a dict."""
        formatted_hops = []

        for hop in hops:
            hop_num = int(hop['hop_num'].strip())
            hosts = hop['hosts'].replace('  ', ' ').strip()

            # Using re.findall(), first we split the hosts, then for each host we store a tuple containing hostname, IP address and the first round-trip time
            # [('<HOSTNAME>', '<IP_ADDRESS>', '<RTT1> ms'), ('<HOSTNAME_N>', '<IP_ADDRESS_N>', '<RTT1_N> ms')]
            hosts = re.findall(r'(?P<hostname>[\w.-]+) \((?P<ip_address>[\d.]+)\) (?P<rtt>\d{1,4}.\d{1,4} ms)', hosts)

            for host in hosts:
                hop_context = {
                    'hop_num': hop_num,
                    'hostname': host[0],
                    'ip_address': host[1],
                    'rtt': host[2],
                }
                self.print_debug(hop_context)
                formatted_hops.append(hop_context)

        return formatted_hops

    def get_geocoded_hops(self, hops):
        """Return hops from get_formatted_hops() with geolocation information
        for each hop."""
        for hop in hops:
            ip_address = hop['ip_address']
            location = None
            if self.locations.has_key(ip_address):
                location = self.locations[ip_address]
            else:
                location = self.get_location(ip_address)
                self.locations[ip_address] = location
            hop['location'] = location

        return hops

    def get_stripped_hops(self, hops):
        """ Return hops from get_geocoded_hops() with each dict containing
        data ready for plotting with e.g. Google Maps JavaScript API."""
        stripped_hops = []

        for hop in hops:
            if hop['location']:
                lat = hop['location']['latitude']
                lon = hop['location']['longitude']
                stripped_hops.append({
                    'hop_num': hop['hop_num'],
                    'ip_address': hop['ip_address'],
                    'latitude': lat,
                    'longitude': lon,
                    'rtt': hop['rtt'],
                })

        return stripped_hops

    def get_location(self, ip_address):
        """Return geolocation information for the specified IP address, e.g.:
            {"ip": "75.126.24.77",
            "hostname": "web365.webfaction.com",
            "isp": "SoftLayer Technologies",
            "organization": "Client Intellect",
            "country": "United States",
            "region": "Texas",
            "city": "Dallas",
            "latitude": 32.9299,
            "longitude": -96.8353}
        """
        location = None
        url = "https://dazzlepod.com/ip/%s.json" % ip_address
        (status_code, json_data) = self.urlopen(url)
        if status_code == 200 and json_data:
            tmp_location = json.loads(json_data)
            if tmp_location.has_key('latitude') and tmp_location.has_key('longitude'):
                location = tmp_location
        return location

    def urlopen(self, url, context = None):
        """Perform HTTP GET/POST on the specified URL and return the resultant
        status code and response.
        """
        status_code = 200

        request = urllib2.Request(url = url)

        if context:
            data = urllib.urlencode(context)
            request.add_data(data)

        response = ''
        try:
            response = urllib2.urlopen(request).read()
        except urllib2.HTTPError, e:
            status_code = e.code
        except urllib2.URLError:
            pass

        try:
            self.urlopen_count += 1
        except AttributeError:
            self.urlopen_count = 1
        self.print_debug("[%d] url = %s, status_code = %d" % (self.urlopen_count, url, status_code))

        return (status_code, response)

    def print_debug(self, msg):
        """Print debug message to standard output."""
        if self.debug:
            print "[DEBUG %s] %s" % (datetime.datetime.now(), msg)


def main():
    usage = """%prog --ip_address=IP_ADDRESS"""
    cmdparser = optparse.OptionParser(usage, version=("traceroute " + __version__))
    cmdparser.add_option("-i", "--ip_address", type="string", default="", help="IP address of destination host")
    cmdparser.add_option("-d", "--debug", action="store_true", default=False, help="Show debug output")

    (options, args) = cmdparser.parse_args()

    if options.ip_address:
        traceroute = Traceroute(ip_address=options.ip_address, debug=options.debug)
        hops = traceroute.traceroute()
        hops = json.dumps(hops, indent=2)
        print hops
    else:
        cmdparser.print_usage()

    return 0


if __name__ == '__main__':
    sys.exit(main())
