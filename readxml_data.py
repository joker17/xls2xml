#!/usr/local/bin/python3
#test for github
import xml.etree.ElementTree as ET
#xml_text = open('data_busin.xml', encoding='utf8').read( )
#root = ET.fromstring(xml_text)
#print (xml_text)

tree = ET.parse('data_busin.xml')
root = tree.getroot()

print ("=============")
for child in root.findall("./items"):
    print(child.tag)
    print(child.get("busin_flag"))
    child.set("busin_flag", "1111")
    print(child.get("busin_flag"))

tree.write("output.xml", encoding="UTF8", xml_declaration="UTF-8")
