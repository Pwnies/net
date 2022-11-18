#!/usr/bin/env python3
import os
import sys
import requests
import csv
import pickle
from collections import defaultdict

DEFAULT_CONFIG_DIR = os.path.expanduser('~/.net')

# MAC prefixes
URL = 'http://standards-oui.ieee.org/oui/oui.csv'
CSV = '.' + os.path.basename(URL)

# Go to script dir
os.chdir(os.path.dirname(__file__))

if '-f' in sys.argv or not os.path.exists(CSV):
    print('Retrieving MAC vendor prefixes from %s' % URL, file=sys.stderr)
    r = requests.get(URL)
    assert r.ok, 'Could not download MAC prefixes'
    open(CSV, 'wb').write(r.text.encode('utf8'))
else:
    print('Using cached MAC vendor prefixes from %s' % CSV, file=sys.stderr)

vendors = defaultdict(list)
with open(CSV, 'r') as f:
    rd = csv.reader(f)
    for row in rd:
        _tag, prefix, vendor, _address = row
        mask = ['??'] * 6
        for i in range(len(prefix) // 2):
            mask[i] = prefix[i * 2: i * 2 + 2].ljust(2, '?')
        mask = ':'.join(mask)
        vendors[vendor].append(mask)

vendors = list(vendors.items())

# Make sure config dir exists
if not os.path.isdir(DEFAULT_CONFIG_DIR):
    print('Creating directory %f' % DEFAULT_CONFIG_DIR, file=sys.stderr)
    os.mkdir(DEFAULT_CONFIG_DIR)

path = os.path.join(DEFAULT_CONFIG_DIR, 'MAC.pkl')
pickle.dump(vendors, open(path, 'wb'))
print('Wrote %d MAC vendor prefixes to %s' % (len(vendors), path), file=sys.stderr)
