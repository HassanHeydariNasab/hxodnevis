# -*- coding: utf-8 -*- 
from __future__ import unicode_literals
from peewee import *
from bs4 import BeautifulSoup, NavigableString
from hazm import *
db = SqliteDatabase("wordsf.db")
db.connect()
class Word(Model):
    word1 = CharField()
    word2 = CharField()

    class Meta:
        database = db
#db.create_tables([Word])
f = open("html/f.html")
fr = f.read()
f.close()
word_list1 = []
word_list2 = []
soup = BeautifulSoup(fr)
all_p = soup.find_all("p")
for i in all_p:
    if type(i.string) is not type(None):
        word_list = word_tokenize(i.string)
        for w in word_list:
            word_list1.append(w)
for i in word_list1:
    word_list2.append(i)
    word_list2.append(i)
for i in range(1, len(word_list2)-1, 2):
    Word(word1 = word_list2[i], word2 = word_list2[i+1]).save()
db.close()
