#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 21:12:23 2019

@author: lz
"""

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        if len(chars) < 1:
            return(0)
        dictionary = {}
        for ch in chars:
            if ch not in dictionary:
                dictionary[ch] = chars.count(ch)
        total = 0
        for word in words:
            add = True
            for cha in word:
                if cha not in dictionary or word.count(cha) > dictionary[cha]:
                    add = False
            if add:
                total += len(word)
        return(total)