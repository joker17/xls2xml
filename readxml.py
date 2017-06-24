#!/usr/local/bin/python3
#test for github
import xml.etree.ElementTree as ET

#xml_text = open('data_busin.xml', encoding='utf8').read( )
xml_text = open('data.xml', encoding='utf8').read( )
print (xml_text)


print ("=============")
root = ET.fromstring(xml_text)
#lists = root.findall(".//items[@busin_flag='2104'")
#lists = root.findall("./singleTable/items")
for child in root.findall("./*/neighbor"):
    print(child.tag)
    print(child.get("name"))
