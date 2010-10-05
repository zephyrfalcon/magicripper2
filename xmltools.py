# xmltools.py

import sys
import xml.sax.saxutils as sux

def pprint_xml(node, indent="", f=sys.stdout):
    """ Pretty-print an ElementTree XML node. (Does not handle attributes.) """
    children = node.getchildren()
    if children:
        f.write("%s<%s>\n" % (indent, node.tag))
        for child in children:
            pprint_xml(child, indent+"  ", f)
        f.write("%s</%s>\n" % (indent, node.tag))
    else:
        f.write(indent)
        f.write("<%s>" % node.tag)
        f.write(sux.escape(node.text or ""))
        f.write("</%s>\n" % node.tag)


