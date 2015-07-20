# -*- coding: utf-8 -*- 
from __future__ import unicode_literals
from peewee import *
from HTMLParser import HTMLParser
from hazm import *

db = SqliteDatabase("wordsf.db")
db.connect()
class Word(Model):
    word1 = CharField()
    word2 = CharField()

    class Meta:
        database = db
db.create_tables([Word])
f = open("html/Fars News Agency.xhtml")
fr = f.read()
f.close()
global word_list
word_list = [] 
class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
	data_d = data.decode("utf-8")
	data_t = word_tokenize(data_d)
	global word_list
	for i in data_t:
		word_list.append(i)
		word_list.append(i)
parser = MyHTMLParser()
parser.feed(fr)
for i in range(1, len(word_list)-1, 2):
	Word(word1 = word_list[i], word2 = word_list[i+1]).save()
