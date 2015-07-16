# -*- coding: utf-8 -*- 
from __future__ import unicode_literals
from peewee import *
from HTMLParser import HTMLParser
from hazm import *

f = open("html/Fars News Agency.xhtml")
fr = f.read()
f.close()
global word_string
word_string = ""
class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
	global word_string
	data_d = data.decode("utf-8")
	data_t = word_tokenize(data_d)
	for i in data_t:
		if ("/" not in i) and (":" not in i):
			word_string = word_string + " " + i
parser = MyHTMLParser()
parser.feed(fr)
word_string = word_string.replace("AM", "PM")
content_list = word_string.split("PM")
for i in content_list:
	content_word_list = i.split(" ")
	for j in len(content_word_list):
		Word(word1 = content_word_list[j] word2 = content_word_list[j + 1])
word_list = word_string.split(" ")
'''while True:
	try:
		word_list.remove("PM")
	except:
		break
while True:
	try:
		word_list.remove("AM")
	except:
		break
'''
print content_list
db = SqliteDatabase("wordsf.db")
db.connect()
class Word(Model):
    word1 = CharField()
    word2 = CharField()

    class Meta:
        database = db

#db.create_tables([Word])

