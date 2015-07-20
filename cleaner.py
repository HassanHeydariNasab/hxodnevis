# -*- coding: utf-8 -*- 
from __future__ import unicode_literals
from peewee import *

db = SqliteDatabase("wordsf.db")
db.connect()
class Word(Model):
    word1 = CharField()
    word2 = CharField()

    class Meta:
        database = db
#db.create_tables([Word])

