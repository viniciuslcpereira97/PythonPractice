#!usr/bin/env python
#-*- coding: utf-8 -*-

# my comparation function
def my_cmp(x, y):
    return -1 if x < y else 0 if x == y else 1

# Test if my comparation is equals built in method
def test(x, y):
    return cmp(x, y) == my_cmp(x, y)

# Define X and Y for test
[x, y] = (1, 1)

# If test function returns True, print result 
if test(x, y):
    # Print my comparation result
    print my_cmp(x, y)