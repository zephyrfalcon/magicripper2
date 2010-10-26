# scan_set.py
# Scan Gatherer to find out which cards are in a set, and create a list of
# multiverse ids for those cards.
# Lists of ids are stored in ids/FOO.txt, where FOO is the short code for an
# expansion set (see sets.py).

import os
import re
import sys
import urllib
#
import sets
import tools

SEARCH_URL = "http://gatherer.wizards.com/Pages/Search/Default.aspx?"\
             "page=%(page)s&set=%%5B%%22%(escaped_set_name)s%%22%%5D"\
             "&special=true"

#URL_RE = re.compile(r"../Card/Details\.aspx\?multiverseid=(\d+)")
URL_RE = re.compile(r"../../Handlers/Image\.ashx\?multiverseid=(\d+)")
# only pick up cards that have their image shown

ALT_VERSION_RE = \
  r"../Card/Details\.aspx\?multiverseid=(\d+)\"><img[^>]+set={0}&.*?>"

class ScannerError(Exception): pass

def scan_set(short_set):
    """ Fetch and scan search result pages for the given set until we don't
        find any more new cards. Return a list of card ids. """
    try:
        full_set_name = sets.set_info[short_set].name
    except KeyError:
        raise ScannerError("Unknown set code: %s" % short_set)
    escaped_set_name = urllib.quote(full_set_name)
    ids = []
    page = 0
    print "Scanning cards for set: %s (%s)" % (short_set, full_set_name)

    while True:
        print "Fetching search results, page", page, "..."
        html = grab_page(page, escaped_set_name)
        new_ids = scan_page(html, short_set)
        old_length = len(ids)
        for new_id in new_ids:
            if new_id not in ids:
                ids.append(new_id)
        if old_length == len(ids):
            break # no new cards found, we're done
        else:
            page += 1

    if len(ids) != sets.set_info[short_set].cards:
        print "WARNING: Expected %d cards, got %d instead" % (
              sets.set_info[short_set].cards, len(ids))

    print "Done;", len(ids), "found"
    return ids

def grab_page(page, escaped_set_name):
    url = SEARCH_URL % locals()
    return tools.grab_url(url)

def scan_page(html, short_set):
    """ Scan the given HTML for URLs to cards, collect their ids, and return
        these ids. """
    ids = []
    for match in URL_RE.finditer(html):
        id = match.group(1)
        ids.append(id)

    # try to find alternate versions (basic lands etc)
    set_re = re.compile(ALT_VERSION_RE.replace('{0}', short_set))
    for match in set_re.finditer(html):
        id = match.group(1)
        ids.append(id)

    # to make things difficult, some sets use aliases here, e.g. 'OD' instead
    # of 'ODY', etc
    alias = sets.set_info[short_set].alias # may be None
    if alias:
        set_re = re.compile(ALT_VERSION_RE.replace('{0}', alias))
        for match in set_re.finditer(html):
            id = match.group(1)
            ids.append(id)

    return ids

def write_ids(short_set, ids):
    filename = os.path.join('ids', "%s.txt" % short_set)
    if not os.path.exists('ids'): os.mkdir('ids')
    f = open(filename, 'wb')
    for id in ids:
        print >> f, id
    f.close()

if __name__ == "__main__":

    for short_set in sys.argv[1:]:
        ids = scan_set(short_set)
        write_ids(short_set, ids)

