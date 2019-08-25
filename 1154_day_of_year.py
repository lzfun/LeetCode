#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 21:54:38 2019

@author: lz
"""

class Solution:
    def dayOfYear(self, date):
        month = int(date[5:7])
        day = int(date[8:10])
        year = int(date[0:4])
        
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        answer = sum(days[:(month-1)]) + day
        
        if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)) and month > 2:
            answer += 1
        
        return(answer)