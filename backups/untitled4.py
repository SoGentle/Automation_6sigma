#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 18:31:42 2020

@author: sogentle
"""

from io import BytesIO
from xml.etree import ElementTree as ET

document = ET.Element('outer')
node = ET.SubElement(document, 'inner')
et = ET.ElementTree(document)

f = BytesIO()
et.write(f, encoding='utf-8', standalone='yes', xml_declaration=True) 
print(f.getvalue())  # your XML file, encoded as UTF-8