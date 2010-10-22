# gen_xml.py

import getopt
import os
import re
import string
import sys
import xml.etree.ElementTree as ET
from BeautifulSoup import BeautifulSoup as BS
#
from cardinfo import CardInfoGatherer
import grab_html
import sanity
import sets
import symbols
import tools
import xmltools

XML_VERSION = "1.1.2"
# this should be bumped up every time a change is made to the XML output
# (directly or indirectly), or if sanity checks were added.

# ElementTree does not write the XML header, so we need to provide this
XML_HEADER = '<?xml version="1.0" ?>'

DEBUG = False

def gen_xml(short_set):
    ids = grab_html.read_ids(short_set)
    root = generate_base_xml(short_set)
    cards = root.find('.//cards')
    for idx, id in enumerate(ids):
        print id
        sp = open_with_bs(short_set, id, 'p')
        so = open_with_bs(short_set, id, 'o')

        try:
            d = gather_data(sp)
        except:
            print "Multiverse id:", id
            raise
        d['type_oracle'], d['rules_oracle'] = extract_oracle_data(so)
        d['multiverseid'] = str(id)
        print d
        sanity.check_card_dict(d)

        add_xml_element(cards, d)
        if DEBUG and idx > 1: break # FIXME

    write_xml(short_set, root)
    print "Done"

ATTRS = ['name', 'manacost', 'type_printed', 'rules_printed',
         'rarity', 'number', 'artist', 'power', 'toughness', 
         'loyalty', 'flavor_text']
SPECIAL = ['manacost']
# these attribute names should correspond to CardInfoGatherer methods and the
# eventual XML tags that we're going to use

def generate_base_xml(short_set):
    s = sets.set_info[short_set]
    root = ET.Element('root')
    meta = ET.SubElement(root, 'meta')
    version = ET.SubElement(meta, 'version')
    version.text = XML_VERSION
    set = ET.SubElement(root, 'set')
    set_name = ET.SubElement(set, 'name')
    set_name.text = s.name
    set_shortname = ET.SubElement(set, 'shortname')
    set_shortname.text = short_set
    noc = ET.SubElement(set, 'number_of_cards')
    noc.text = str(s.cards)
    date = ET.SubElement(set, 'release_date')
    date.text = s.date
    cards = ET.SubElement(set, 'cards')
    return root

def gather_data(soup):
    d = {}
    cig = CardInfoGatherer(soup)
    for attr in ATTRS:
        value = getattr(cig, attr)()
        if value is not None:
            d[attr] = value

    return d

def extract_oracle_data(soup):
    cig = CardInfoGatherer(soup)
    return cig.type_printed(), cig.rules_printed()

def open_with_bs(short_set, id, suffix):
    path = os.path.join('html', short_set, "%s-%s.html" % (id, suffix))
    with open(path, 'rb') as f:
        data = f.read()
    return BS(data)

def add_xml_element(elem, d):
    card = ET.SubElement(elem, 'card')

    for key, value in d.items():
        if key in SPECIAL: continue
        x = ET.SubElement(card, key)
        x.text = value

    manacost = ET.SubElement(card, 'manacost')
    for symbol in d['manacost']:
        s = ET.SubElement(manacost, 'symbol')
        s.text = symbol

    return card

def write_xml(short_set, root):
    if not os.path.exists('xml'): os.makedirs('xml')
    print "Writing XML..."
    path = os.path.join('xml', short_set + ".xml")
    with open(path, 'wb') as f:
        f.write(XML_HEADER + "\n")
        xmltools.pprint_xml(root, f=f)

    sanity.validate_xml(path)

re_version = re.compile("<version>(.*?)</version>")

def find_updates():
    """ Return the sets whose XML files needs updated, i.e. they have a
        version < the latest version. """
    behind = []
    for short_set in sets.set_info.keys():
        path = os.path.join("xml", short_set + ".xml")
        with open(path, 'rb') as f:
            chunk = f.read(2048) # read first 2K
        m = re_version.search(chunk)
        if m:
            file_version = m.group(1)
            if file_version < XML_VERSION:
                behind.append(short_set)
        else:
            # no version?! must be really old
            behind.append(short_set)

    return behind


if __name__ == "__main__":

    opts, args = getopt.getopt(sys.argv[1:], "du", ["update"])
    if args == ["all"]:
        args = sorted(sets.set_info.keys())

    for o, a in opts:
        if o == '-d':
            print "Running in debug mode"
            DEBUG = True
        elif o in ("--update", "-u"):
            args = find_updates()
            print "Updating:", args

    for short_set in args:
        gen_xml(short_set)

