#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 23:39:25 2019

@author: lz
"""

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        number = ""
        for ch in s:
            if ch.isdigit():
                number += ch
            elif ch == '[':
                stack.append(ch)
                stack.append(number)
                print(stack)
                number = ""
            elif ch == ']':
                word = ""
                while stack[-1] != '[':
                    top = stack.pop()
                    print(stack)
                    if top.isdigit():
                        word = int(top) * word
                    else:
                        word = top + word
                stack[-1] = word
                print(stack)
            else:
                stack.append(ch)
                print(stack)
        return("".join(stack))