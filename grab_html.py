# grab_html.py
# For a given set, grab the Gatherer HTML source for each card, and store it
# in a directory html/FOO/, where FOO is the given set. No parsing or
# information extraction is done at this point.

from __future__ import with_statement
import os
import re
import sys
#
import tools

CARD_URL = "http://gatherer.wizards.com/Pages/Card/Details.aspx?"\
           "multiverseid=%(id)s&printed=%(printed)s"

re_card_name = re.compile(r"<title>\s*(.*?)\(")

def grab_html(short_set):
    ids = read_ids(short_set)
    for idx, id in enumerate(ids):
        for printed in ('true', 'false'):
            url = CARD_URL % locals()
            html = tools.grab_url(url)
            write_html(id, html, short_set, printed)
        card_name = extract_card_name(html)
        print "Grabbed card:\t%d\t(%3d/%d)\t%s" % (id, idx+1, len(ids),
              card_name)
    print "Done"

def read_ids(short_set):
    filename = os.path.join('ids', short_set + ".txt")
    f = open(filename, 'rb')
    ids = [int(line) for line in f.readlines() if line.strip()]
    f.close()
    return ids

def write_html(id, html, short_set, printed):
    path = os.path.join('html', short_set)
    if not os.path.exists(path): os.makedirs(path)
    p = 'p' if printed == 'true' else 'o'
    filename = os.path.join(path, "%s-%s.html" % (id, p))
    with open(filename, 'wb') as f:
        f.write(html)

def extract_card_name(html):
    m = re_card_name.search(html)
    if m:
        return m.group(1).strip()
    else:
        return "?"

if __name__ == "__main__":

    for short_set in sys.argv[1:]:
        grab_html(short_set)

