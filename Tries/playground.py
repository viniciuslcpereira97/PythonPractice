#!usr/bin/env python
#-*- coding: utf-8 -*-

from Trie import Trie

myTrie = Trie()

names = [
    'abc',
    'abcd',
    'abcde',
    'aceg',
    'acfp',
    'adef',
]

for name in names:
    myTrie.insert(name)

# myTrie.check()
myTrie.countSimilars('ab')
