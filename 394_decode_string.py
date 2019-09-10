#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 23:39:25 2019

@author: lz
"""

class Solution:
    def decodeString(self, s: str) -> str:
        if len(s) < 1:
            return("")
        repeatN = []
        strings = []
        stack = []
        answer = ""
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = s[i]
                while s[i+1].isdigit():
                    i += 1
                    num += s[i+1]
                repeatN.append(int(num))
                i += 1
            elif s[i].isalpha():
                string = s[i]
                while s[i+1].isalpha():
                    i += 1
                    string += s[i+1]
                strings.append(string)
                i += 1
            elif s[i] == "[":
                stack.append(s[i])
                i += 1
            else:
                if len(stack) == 1:
                    answer += repeatN[-1]*strings[-1]
                    del repeatN[-1]
                    del strings[-1]
                    del stack[-1]
                    i += 1
                else:
                    string = repeatN[-1]*strings[-1]
                    del repeatN[-1]
                    del strings[-1]
                    del stack[-1]
                    strings[-1] += string
                    i += 1
                    
        if len(strings) > 0:
            answer += "".join(strings)
        return(answer)