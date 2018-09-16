import json
import include_def

def sortByLength(inputStr):
  return len(inputStr)

text_list = []
text_lst = []

with open('Files/newsafr.json') as datafile:
  json_data = json.load(datafile)

for item in json_data['rss']['channel']['items']:
  text_list += item['description'].split(' ')

text_list.sort(key=sortByLength, reverse=True)
words_dict = include_def.descriptions_len_list(text_list)
include_def.words_top(words_dict)