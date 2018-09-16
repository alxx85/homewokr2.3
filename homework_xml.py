import xml.etree.ElementTree as ET
import include_def

trees = ET.parse('Files/newsafr.xml')
descriptions = []
description_len = []
root = trees.getroot()
xml_items = root.findall("channel/item")

for item in xml_items:
    description = item.find("description")
    descriptions += description.text.split(" ")

def sortByLength(inputStr):
    return len(inputStr)

descriptions.sort(key=sortByLength, reverse=True)
words_dict = include_def.descriptions_len_list(descriptions)
include_def.words_top(words_dict)