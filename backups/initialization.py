#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 21:00:57 2020

@author: sogentle
"""


import xml.etree.ElementTree as ET

tree = ET.parse('./model04.xml')

root = tree.getroot()
element = root[0]

# class PCB(object):
#     def __init__(self):
        