#!usr/bin/env python
#-*- coding: utf-8 -*-

import json

class Trie(object):

    def __init__(self):
        self.root = {}

    def insert(self, word):
        trie = self.root
        current_dict = trie
        for let in word:
            current_dict = current_dict.setdefault(let, {})
        current_dict['__end__'] = True

    def countSimilars(self, partial):
        trie = self.root
        for let in partial:
            trie = trie.setdefault(let)
        self.iterateThroughSimilars(trie)

    def iterateThroughSimilars(self, trie):
        for key, itens in trie.items():
            print key
            print itens

    def check(self):
        print self.root
