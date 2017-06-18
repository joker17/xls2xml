#!/usr/local/bin/python3
#test for github
import xml.etree.ElementTree as ET
tree = ET.parse('data.xml')
root = tree.getroot()
print(root.tag)