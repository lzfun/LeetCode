#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 19:07:09 2019

@author: lz
"""

def function4Fun():
    yield 1
    yield 2
    yield 3
    
for i in function4Fun():
    print(i)