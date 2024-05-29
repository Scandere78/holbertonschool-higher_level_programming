#!/usr/bin/python3

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):

    root = ET.Element('data')
    for key, val in dictionary.items():
        child = ET.Element(key)
        child.text = str(val)
        root.append(child)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def serialize_to_xml(dictionary, filename):

    tree = ET.parse(filname)
    root = tree.getroot()

    _dict = {}
    for child in root:
        _dict[child.tag] = child.text
    return _dict
