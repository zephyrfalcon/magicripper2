# grab_images.py

from __future__ import with_statement
import os
import sys
#
import grab_html
import tools

IMAGE_URL = "http://gatherer.wizards.com/Handlers/Image.ashx?"\
            "multiverseid=%(id)s&type=card"

def grab_images(short_set):
    """ Download all card images for the given set. """

    path = os.path.join('images', short_set)
    if not os.path.exists(path):
        os.makedirs(path)

    ids = grab_html.read_ids(short_set)
    for idx, id in enumerate(ids):
        url = IMAGE_URL % locals()
        data = tools.grab_url(url)
        print "Grabbed image: %s" % id
        write_image(short_set, id, data)

def write_image(short_set, id, data):
    path = os.path.join('images', short_set, '%s.jpg' % id) # assume JPG
    with open(path, 'wb') as f:
        f.write(data)


if __name__ == "__main__":

    for short_set in sys.argv[1:]:
        grab_images(short_set)
    
