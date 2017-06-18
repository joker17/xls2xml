#!/usr/local/bin/python3
import xml.etree.ElementTree as ET
tree = ET.parse('data.xml')
root = tree.getroot()
print(root.tag)