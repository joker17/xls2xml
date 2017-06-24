#!/usr/local/bin/python3
#test for github
import xml.etree.ElementTree as ET
tree = ET.parse('data.xml')
root = tree.getroot()
print(root.tag)
for child in root:
    print(child.tag, child.attrib)

for child in root.findall("./*/neighbor"):
    print(child.tag)