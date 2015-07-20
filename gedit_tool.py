# -*- coding: utf-8 -*- 
from __future__ import unicode_literals
import unicodedata
import sys
from peewee import *
db = SqliteDatabase("wordsf.db")
db.connect()
class Word(Model):
    word1 = CharField()
    word2 = CharField()

    class Meta:
        database = db
word1 =  sys.argv[1]
#db.create_tables([Word])
word2 = Word.get(Word.word1 == word1).word2
word2 = word2.encode('utf-8')
sys.stdout.write(" ")
sys.stdout.write(word2)
