# -*- coding: utf-8 -*- 
from __future__ import unicode_literals
import unicodedata
import sys
import os
from peewee import *
import subprocess
from random import random

db = SqliteDatabase('%s/hxodnevis/wordsf.db'%(os.environ.get('HOME')))
db.connect()
class Word(Model):
    word1 = CharField()
    word2 = CharField()
    class Meta:
        database = db
word1 =  sys.argv[1]
f = []
f2 = {}
p = []
for word1 in Word.select().where(Word.word1 == word1):
    f.append(word1.word2.encode('utf-8'))
f_u = list(set(f))
for i in f_u:
    f2[i] = f.count(i)
for w in sorted(f2, key=f2.get, reverse=True):
    #print w, f2[w]
    p.append(w)
len_p = len(p)
if len_p == 0:
    pass
elif len_p== 1:
    #p[0] = p[0][0:-1]
    sys.stdout.write(" ")
    sys.stdout.write(p[0])
elif len_p == 2:
    c = "gxmessage -encoding utf-8 -print -center -buttons '%s','%s' 'انتخاب کنید'"%(p[0].decode('utf-8'), p[1].decode('utf-8'))
    pp = subprocess.Popen(c, stdout=subprocess.PIPE, shell=True)
    (output, err) = pp.communicate()
    output = output[0:-1]
    sys.stdout.write(" ")
    sys.stdout.write(output)
else:
    r1 = int(random()*2)
    if len_p > 4:
        r2 = int(random()*5)
        while r2 == r1:
            r2 = int(random()*5)
        r3 = int(random()*len_p)
        while r3 == r1:
            r3 = int(random()*len_p)
        while r3 == r2:
            r3 = int(random()*len_p)
    elif len_p == 3:
        r1 = 0
        r2 = 1
        r3 = 2
    elif len_p == 4:
        r2 = int(random()*4)
        while r2 == r1:
            r2 = int(random()*4)
        r3 = int(random()*4)
        while r3 == r1:
            r3 = int(random()*4)
        while r3 == r2:
            r3 = int(random()*4)
    c = "gxmessage -encoding utf-8 -print -center -buttons '%s','%s',' %s' 'انتخاب کنید'"%(p[r1].decode('utf-8'), p[r2].decode('utf-8'), p[r3].decode('utf-8'))
    pp = subprocess.Popen(c, stdout=subprocess.PIPE, shell=True)
    (output, err) = pp.communicate()
    output = output[0:-1]
    sys.stdout.write(" ")
    sys.stdout.write(output)
db.close()
