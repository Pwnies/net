#!/usr/bin/env python2.7
import os
import sys
import requests
import csv
try:
    import cPickle as pickle
except ImportError:
    import pickle
from collections import defaultdict

DEFAULT_CONFIG_DIR = os.path.expanduser('~/.net')

# MAC prefixes
URL = 'http://standards-oui.ieee.org/oui/oui.csv'
CSV = '.' + os.path.basename(URL)

# Go to script dir
os.chdir(os.path.dirname(__file__))

if '-f' in sys.argv or not os.path.exists(CSV):
    print >>sys.stderr, 'Retrieving MAC vendor prefixes from %s' % URL
    r = requests.get(URL)
    assert r.ok, 'Could not download MAC prefixes'
    file(CSV, 'wb').write(r.text.encode('utf8'))
else:
    print >>sys.stderr, 'Using cached MAC vendor prefixes from %s' % CSV

vendors = defaultdict(list)
with file(CSV, 'rb') as f:
    rd = csv.reader(f)
    for row in rd:
        _tag, prefix, vendor, _address = row
        mask = ['??'] * 6
        for i in xrange(len(prefix) / 2):
            mask[i] = prefix[i * 2: i * 2 + 2].ljust(2, '?')
        mask = ':'.join(mask)
        vendors[vendor].append(mask)

vendors = vendors.items()

# Make sure config dir exists
if not os.path.isdir(DEFAULT_CONFIG_DIR):
    print >>sys.stderr, 'Creating directory %f' % DEFAULT_CONFIG_DIR
    os.mkdir(DEFAULT_CONFIG_DIR)

path = os.path.join(DEFAULT_CONFIG_DIR, 'MAC.pkl')
pickle.dump(vendors, file(path, 'wb'))
print >>sys.stderr, 'Wrote %d MAC vendor prefixes to %s' % (len(vendors), path)
