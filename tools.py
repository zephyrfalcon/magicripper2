# tools.py

import sys
import urllib

def grab_url(url):
    u = urllib.urlopen(url)
    data = u.read()
    u.close()
    return data

