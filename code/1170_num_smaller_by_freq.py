#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 21:57:21 2019

@author: lz
"""

class Solution:
    def numSmallerByFrequency(self, queries, words):
        length = len(words)
        
        num_words = [0]*length
        num_queries = [0]*len(queries)
        answer = [0]*len(queries)
        
        for i in range(length):
            num_words[i] = self.f(words[i])
        num_words.sort()
        
        for j in range(len(queries)):
            num_queries[j] = self.f(queries[j])

        for i in range(length):
            for j in range(len(queries)):
                if num_queries[j] < num_words[0]:
                    answer[j] = length
                elif answer[j] == 0 and num_queries[j] < num_words[i]:
                    answer[j] = length - i
        return(answer)
        
    def f(self, s):
        d = {}
        for ch in s:
            if ch not in d:
                d[ch] = 1
            else:
                d[ch] += 1
        return(d[min(d.keys())])