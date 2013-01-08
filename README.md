# traceroute
Traceroute is a Python script that allows you to get traceroute results with associated geolocation information for each hop for a specified host from geographically distant source(s).

## Installation

Save traceroute.py into a directory with its path stored in your PYTHONPATH environment variable.

## Usage

Try the following from your Python interpreter:

    >>> from traceroute import Traceroute
    >>> traceroute = Traceroute(ip_address='8.8.8.8')
    >>> hops = traceroute.traceroute()
    >>> hops
    [{'latitude': 40.3756, 'rtt': '0.862 ms', 'ip_address': '128.112.128.114', 'longitude': -74.6597, 'hop_num': 1}, {'latitude': 40.3756, 'rtt': '0.462 ms', 'ip_address': '128.112.12.22', 'longitude': -74.6597, 'hop_num': 2}, {'latitude': 40.3265, 'rtt': '8.374 ms', 'ip_address': '24.104.128.89', 'longitude': -75.3697, 'hop_num': 3}, {'latitude': 38.0, 'rtt': '21.010 ms', 'ip_address': '68.86.84.177', 'longitude': -97.0, 'hop_num': 4}, {'latitude': 38.0, 'rtt': '12.218 ms', 'ip_address': '68.86.86.70', 'longitude': -97.0, 'hop_num': 5}, {'latitude': 38.0, 'rtt': '31.103 ms', 'ip_address': '75.149.231.62', 'longitude': -97.0, 'hop_num': 6}, {'latitude': 37.4192, 'rtt': '14.752 ms', 'ip_address': '209.85.252.80', 'longitude': -122.0574, 'hop_num': 7}, {'latitude': 37.4192, 'rtt': '18.437 ms', 'ip_address': '72.14.238.18', 'longitude': -122.0574, 'hop_num': 9}, {'latitude': 37.4192008972168, 'rtt': '18.610 ms', 'ip_address': '72.14.238.70', 'longitude': -122.05740356445312, 'hop_num': 9}, {'latitude': 37.4192, 'rtt': '16.696 ms', 'ip_address': '72.14.238.18', 'longitude': -122.0574, 'hop_num': 9}, {'latitude': 37.4192, 'rtt': '24.441 ms', 'ip_address': '72.14.232.21', 'longitude': -122.0574, 'hop_num': 10}, {'latitude': 37.4192, 'rtt': '13.925 ms', 'ip_address': '216.239.49.149', 'longitude': -122.0574, 'hop_num': 10}, {'latitude': 37.4192, 'rtt': '19.800 ms', 'ip_address': '72.14.232.21', 'longitude': -122.0574, 'hop_num': 10}, {'latitude': 37.4192, 'rtt': '14.144 ms', 'ip_address': '8.8.8.8', 'longitude': -122.0574, 'hop_num': 11}]
    >>> import json
    >>> json.dumps(hops, indent=2)
    '[\n  {\n    "latitude": 40.3756, \n    "rtt": "0.862 ms", \n    "ip_address": "128.112.128.114", \n    "longitude": -74.6597, \n    "hop_num": 1\n  }, \n  {\n    "latitude": 40.3756, \n    "rtt": "0.462 ms", \n    "ip_address": "128.112.12.22", \n    "longitude": -74.6597, \n    "hop_num": 2\n  }, \n  {\n    "latitude": 40.3265, \n    "rtt": "8.374 ms", \n    "ip_address": "24.104.128.89", \n    "longitude": -75.3697, \n    "hop_num": 3\n  }, \n  {\n    "latitude": 38.0, \n    "rtt": "21.010 ms", \n    "ip_address": "68.86.84.177", \n    "longitude": -97.0, \n    "hop_num": 4\n  }, \n  {\n    "latitude": 38.0, \n    "rtt": "12.218 ms", \n    "ip_address": "68.86.86.70", \n    "longitude": -97.0, \n    "hop_num": 5\n  }, \n  {\n    "latitude": 38.0, \n    "rtt": "31.103 ms", \n    "ip_address": "75.149.231.62", \n    "longitude": -97.0, \n    "hop_num": 6\n  }, \n  {\n    "latitude": 37.4192, \n    "rtt": "14.752 ms", \n    "ip_address": "209.85.252.80", \n    "longitude": -122.0574, \n    "hop_num": 7\n  }, \n  {\n    "latitude": 37.4192, \n    "rtt": "18.437 ms", \n    "ip_address": "72.14.238.18", \n    "longitude": -122.0574, \n    "hop_num": 9\n  }, \n  {\n    "latitude": 37.4192008972168, \n    "rtt": "18.610 ms", \n    "ip_address": "72.14.238.70", \n    "longitude": -122.05740356445312, \n    "hop_num": 9\n  }, \n  {\n    "latitude": 37.4192, \n    "rtt": "16.696 ms", \n    "ip_address": "72.14.238.18", \n    "longitude": -122.0574, \n    "hop_num": 9\n  }, \n  {\n    "latitude": 37.4192, \n    "rtt": "24.441 ms", \n    "ip_address": "72.14.232.21", \n    "longitude": -122.0574, \n    "hop_num": 10\n  }, \n  {\n    "latitude": 37.4192, \n    "rtt": "13.925 ms", \n    "ip_address": "216.239.49.149", \n    "longitude": -122.0574, \n    "hop_num": 10\n  }, \n  {\n    "latitude": 37.4192, \n    "rtt": "19.800 ms", \n    "ip_address": "72.14.232.21", \n    "longitude": -122.0574, \n    "hop_num": 10\n  }, \n  {\n    "latitude": 37.4192, \n    "rtt": "14.144 ms", \n    "ip_address": "8.8.8.8", \n    "longitude": -122.0574, \n    "hop_num": 11\n  }\n]'
    >>>

You can also run the script directly by passing in the --ip_address option:

    $ python traceroute.py --ip_address=8.8.8.8
    [
      {
        "latitude": 40.3756,
        "rtt": "0.862 ms",
        "ip_address": "128.112.128.114",
        "longitude": -74.6597,
        "hop_num": 1
      },
      {
        "latitude": 40.3756,
        "rtt": "0.462 ms",
        "ip_address": "128.112.12.22",
        "longitude": -74.6597,
        "hop_num": 2
      },
      {
        "latitude": 40.3265,
        "rtt": "8.374 ms",
        "ip_address": "24.104.128.89",
        "longitude": -75.3697,
        "hop_num": 3
      },
      {
        "latitude": 38.0,
        "rtt": "21.010 ms",
        "ip_address": "68.86.84.177",
        "longitude": -97.0,
        "hop_num": 4
      },
      {
        "latitude": 38.0,
        "rtt": "12.218 ms",
        "ip_address": "68.86.86.70",
        "longitude": -97.0,
        "hop_num": 5
      },
      {
        "latitude": 38.0,
        "rtt": "31.103 ms",
        "ip_address": "75.149.231.62",
        "longitude": -97.0,
        "hop_num": 6
      },
      {
        "latitude": 37.4192,
        "rtt": "14.752 ms",
        "ip_address": "209.85.252.80",
        "longitude": -122.0574,
        "hop_num": 7
      },
      {
        "latitude": 37.4192,
        "rtt": "18.437 ms",
        "ip_address": "72.14.238.18",
        "longitude": -122.0574,
        "hop_num": 9
      },
      {
        "latitude": 37.4192008972168,
        "rtt": "18.610 ms",
        "ip_address": "72.14.238.70",
        "longitude": -122.05740356445312,
        "hop_num": 9
      },
      {
        "latitude": 37.4192,
        "rtt": "16.696 ms",
        "ip_address": "72.14.238.18",
        "longitude": -122.0574,
        "hop_num": 9
      },
      {
        "latitude": 37.4192,
        "rtt": "24.441 ms",
        "ip_address": "72.14.232.21",
        "longitude": -122.0574,
        "hop_num": 10
      },
      {
        "latitude": 37.4192,
        "rtt": "13.925 ms",
        "ip_address": "216.239.49.149",
        "longitude": -122.0574,
        "hop_num": 10
      },
      {
        "latitude": 37.4192,
        "rtt": "19.800 ms",
        "ip_address": "72.14.232.21",
        "longitude": -122.0574,
        "hop_num": 10
      },
      {
        "latitude": 37.4192,
        "rtt": "14.144 ms",
        "ip_address": "8.8.8.8",
        "longitude": -122.0574,
        "hop_num": 11
      }
    ]
