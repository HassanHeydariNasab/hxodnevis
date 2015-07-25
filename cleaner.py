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
Word.delete().where(Word.word1 == "PM").execute()
Word.delete().where(Word.word1 == "AM").execute()
Word.delete().where(Word.word1 == "،").execute()
Word.delete().where(Word.word1 == ":").execute()
Word.delete().where(Word.word1 == "«").execute()
Word.delete().where(Word.word1 == "»").execute()
Word.delete().where(Word.word1 == "(").execute()
Word.delete().where(Word.word1 == ")").execute()
Word.delete().where(Word.word1 == ">").execute()
Word.delete().where(Word.word1 == "<").execute()
Word.delete().where(Word.word1 == "]").execute()
Word.delete().where(Word.word1 == "[").execute()
Word.delete().where(Word.word1 == ".").execute()
Word.delete().where(Word.word1 == "؛").execute()
Word.delete().where(Word.word1 == "%htmlDTD;").execute()
Word.delete().where(Word.word1 == "%feedDTD;").execute()
Word.delete().where(Word.word1 == ";").execute()
Word.delete().where(Word.word1.contains("2015")).execute()
Word.delete().where(Word.word1.contains("/")).execute()
db.close()

