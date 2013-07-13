# traceroute
Multi-source traceroute with geolocation information. Demo: [IP Address Lookup](http://dazzlepod.com/ip/) (under "Visual Traceroute" tab)

![Using output from traceroute.py to plot hops on Google Map](https://raw.github.com/ayeowch/traceroute/master/screenshot.png)

## Installation

Save traceroute.py into a directory with its path stored in your PYTHONPATH environment variable.

## Usage

Try the following from your Python interpreter:

    >>> from traceroute import Traceroute
    >>> traceroute = Traceroute("8.8.8.8")
    >>> hops = traceroute.traceroute()
    >>> hops
    [{'hostname': 'gigagate1', 'longitude': -74.6597, 'rtt': '0.913 ms', 'hop_num': 1, 'latitude': 40.3756, 'ip_address': '128.112.128.114'}, {'hostname': 'vgate1', 'longitude': -74.6597, 'rtt': '0.498 ms', 'hop_num': 2, 'latitude': 40.3756, 'ip_address': '128.112.12.22'}, {'hostname': '38.122.150.1', 'longitude': -74.006, 'rtt': '4.087 ms', 'hop_num': 3, 'latitude': 40.7143, 'ip_address': '38.122.150.1'}, {'hostname': 'te4-3.ccr01.phl01.atlas.cogentco.com', 'longitude': -97.0, 'rtt': '3.469 ms', 'hop_num': 4, 'latitude': 38.0, 'ip_address': '66.28.4.233'}, {'hostname': 'te7-3.ccr01.phl01.atlas.cogentco.com', 'longitude': -97.0, 'rtt': '3.586 ms', 'hop_num': 4, 'latitude': 38.0, 'ip_address': '154.54.0.189'}, {'hostname': 'te4-1.ccr01.bwi01.atlas.cogentco.com', 'longitude': -97.0, 'rtt': '6.470 ms', 'hop_num': 5, 'latitude': 38.0, 'ip_address': '154.54.2.173'}, {'hostname': 'te7-2.ccr01.bwi01.atlas.cogentco.com', 'longitude': -97.0, 'rtt': '6.821 ms', 'hop_num': 5, 'latitude': 38.0, 'ip_address': '154.54.83.222'}, {'hostname': 'te4-1.ccr01.bwi01.atlas.cogentco.com', 'longitude': -97.0, 'rtt': '20.586 ms', 'hop_num': 5, 'latitude': 38.0, 'ip_address': '154.54.2.173'}, {'hostname': '38.122.63.14', 'longitude': -83.1763, 'rtt': '34.924 ms', 'hop_num': 8, 'latitude': 42.3223, 'ip_address': '38.122.63.14'}, {'hostname': '38.122.62.74', 'longitude': -95.3877, 'rtt': '8.072 ms', 'hop_num': 8, 'latitude': 29.6144, 'ip_address': '38.122.62.74'}, {'hostname': '38.122.63.14', 'longitude': -83.1763, 'rtt': '8.950 ms', 'hop_num': 8, 'latitude': 42.3223, 'ip_address': '38.122.63.14'}, {'hostname': '209.85.252.80', 'longitude': -122.0574, 'rtt': '20.619 ms', 'hop_num': 9, 'latitude': 37.4192, 'ip_address': '209.85.252.80'}, {'hostname': '209.85.252.46', 'longitude': -122.0574, 'rtt': '13.415 ms', 'hop_num': 9, 'latitude': 37.4192, 'ip_address': '209.85.252.46'}, {'hostname': '72.14.234.65', 'longitude': -74.006, 'rtt': '15.676 ms', 'hop_num': 12, 'latitude': 40.7143, 'ip_address': '72.14.234.65'}, {'hostname': '72.14.234.53', 'longitude': -122.0574, 'rtt': '16.844 ms', 'hop_num': 12, 'latitude': 37.4192, 'ip_address': '72.14.234.53'}, {'hostname': 'google-public-dns-a.google.com', 'longitude': -97.0, 'rtt': '16.960 ms', 'hop_num': 14, 'latitude': 38.0, 'ip_address': '8.8.8.8'}]
    >>>

You can also run the script directly by passing in the --ip_address option:

    $ python traceroute.py --help
    Usage: traceroute.py --ip_address=IP_ADDRESS

    Options:
      -h, --help            show this help message and exit
      -i IP_ADDRESS, --ip_address=IP_ADDRESS
                            IP address of destination host (default: 8.8.8.8)
      -j JSON_FILE, --json_file=JSON_FILE
                            List of sources in JSON file (default: sources.json)
      -c COUNTRY, --country=COUNTRY
                            Traceroute will be initiated from this country; choose
                            'LO' for localhost to run traceroute locally, 'BY' for
                            Belarus, 'CH' for Switzerland, 'JP' for Japan, 'RU'
                            for Russia, 'UK' for United Kingdom or 'US' for United
                            States (default: US)
      -t TMP_DIR, --tmp_dir=TMP_DIR
                            Temporary directory to store downloaded traceroute
                            results (default: /tmp)
      -n, --no_geo          No geolocation data (default: False)
      -s TIMEOUT, --timeout=TIMEOUT
                            Timeout in seconds for all downloads (default: 120)
      -d, --debug           Show debug output (default: False)

    $ python traceroute.py --ip_address=8.8.8.8
    [
        {
            "hostname": "gigagate1",
            "longitude": -74.6597,
            "rtt": "0.913 ms",
            "hop_num": 1,
            "latitude": 40.3756,
            "ip_address": "128.112.128.114"
        },
        {
            "hostname": "vgate1",
            "longitude": -74.6597,
            "rtt": "0.498 ms",
            "hop_num": 2,
            "latitude": 40.3756,
            "ip_address": "128.112.12.22"
        },
        {
            "hostname": "38.122.150.1",
            "longitude": -74.006,
            "rtt": "4.087 ms",
            "hop_num": 3,
            "latitude": 40.7143,
            "ip_address": "38.122.150.1"
        },
        {
            "hostname": "te4-3.ccr01.phl01.atlas.cogentco.com",
            "longitude": -97.0,
            "rtt": "3.469 ms",
            "hop_num": 4,
            "latitude": 38.0,
            "ip_address": "66.28.4.233"
        },
        {
            "hostname": "te7-3.ccr01.phl01.atlas.cogentco.com",
            "longitude": -97.0,
            "rtt": "3.586 ms",
            "hop_num": 4,
            "latitude": 38.0,
            "ip_address": "154.54.0.189"
        },
        {
            "hostname": "te4-1.ccr01.bwi01.atlas.cogentco.com",
            "longitude": -97.0,
            "rtt": "6.470 ms",
            "hop_num": 5,
            "latitude": 38.0,
            "ip_address": "154.54.2.173"
        },
        {
            "hostname": "te7-2.ccr01.bwi01.atlas.cogentco.com",
            "longitude": -97.0,
            "rtt": "6.821 ms",
            "hop_num": 5,
            "latitude": 38.0,
            "ip_address": "154.54.83.222"
        },
        {
            "hostname": "te4-1.ccr01.bwi01.atlas.cogentco.com",
            "longitude": -97.0,
            "rtt": "20.586 ms",
            "hop_num": 5,
            "latitude": 38.0,
            "ip_address": "154.54.2.173"
        },
        {
            "hostname": "38.122.63.14",
            "longitude": -83.1763,
            "rtt": "34.924 ms",
            "hop_num": 8,
            "latitude": 42.3223,
            "ip_address": "38.122.63.14"
        },
        {
            "hostname": "38.122.62.74",
            "longitude": -95.3877,
            "rtt": "8.072 ms",
            "hop_num": 8,
            "latitude": 29.6144,
            "ip_address": "38.122.62.74"
        },
        {
            "hostname": "38.122.63.14",
            "longitude": -83.1763,
            "rtt": "8.950 ms",
            "hop_num": 8,
            "latitude": 42.3223,
            "ip_address": "38.122.63.14"
        },
        {
            "hostname": "209.85.252.80",
            "longitude": -122.0574,
            "rtt": "20.619 ms",
            "hop_num": 9,
            "latitude": 37.4192,
            "ip_address": "209.85.252.80"
        },
        {
            "hostname": "209.85.252.46",
            "longitude": -122.0574,
            "rtt": "13.415 ms",
            "hop_num": 9,
            "latitude": 37.4192,
            "ip_address": "209.85.252.46"
        },
        {
            "hostname": "72.14.234.65",
            "longitude": -74.006,
            "rtt": "15.676 ms",
            "hop_num": 12,
            "latitude": 40.7143,
            "ip_address": "72.14.234.65"
        },
        {
            "hostname": "72.14.234.53",
            "longitude": -122.0574,
            "rtt": "16.844 ms",
            "hop_num": 12,
            "latitude": 37.4192,
            "ip_address": "72.14.234.53"
        },
        {
            "hostname": "google-public-dns-a.google.com",
            "longitude": -97.0,
            "rtt": "16.960 ms",
            "hop_num": 14,
            "latitude": 38.0,
            "ip_address": "8.8.8.8"
        }
    ]

## License
Copyright (c) 2013 Addy Yeow Chin Heng &lt;ayeowch@gmail.com&gt;

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
