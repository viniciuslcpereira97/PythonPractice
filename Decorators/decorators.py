#!usr/bin/env python
#-*- coding: utf-8 -*-

def makebold(fn):
    def t():
        return "<b>" + fn() + "</b>"
    return t

def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makebold
@makeitalic
def hello():
    return "hello world"

print hello()