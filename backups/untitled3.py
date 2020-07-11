#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 00:09:42 2020

@author: sogentle
"""


import xml.etree.ElementTree as ET

fields = """
<fields>
<Temp>
</Temp>
</fields>
"""
#Insert new field into <fields>
root = ET.fromstring(fields)
# print(root.tag)
temp = root.find('Temp')

new_field = ET.Element("field")
field_col = ET.SubElement(new_field, "column")
# field_col.text ="TEST"
field_des = ET.SubElement(new_field, "description")
field_data = ET.SubElement(new_field, "datatype")
field_length = ET.SubElement(new_field, "length")
# root.insert(1, new_field)
temp.insert(0, new_field)
ET.dump(root)
tree = ET.ElementTree(root)
tree.write(open('test.xml','w'), encoding='unicode')