#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 15:42:58 2019

@author: lz
"""
class Solution:
    def numDecodings(self, s):
        answer = [0]*(len(s)+1)
        
        if 0 < int(s[0]) <= 9:
            answer[0] = 1
            
        else:
            answer[0] = 0
            
        answer[-1] = 1
        
        for i in range(1, len(s)):
            if answer[i-1] == 0:
                return(0)
            else:
                if 0 < int(s[i]) <= 9:
                    answer[i] += answer[i-1]
                    
                else:
                    answer[i] += 0
                    
                if 10 <= int(s[i-1:i+1]) <= 26:
                    answer[i] += answer[i-2]
                      
                else:
                    answer[i] += 0
                    
        return(answer[-2])

"""
#Faster solution 1
class Solution:
    def numDecodings(self, s):
        previous_ways, ways, previous_chr = 0, int(s>''), ''
        for chr in s:
            previous_ways, ways, previous_chr = ways, (chr > '0') * ways + (9 < int(previous_chr + chr) < 27) * previous_ways, chr

        return ways
"""
      
"""
#Faster solution 2
class Solution:
    def numDecodings(self, s):
        if s == "":
            return 0
        n = len(s)
        cache = [0 for i in range(len(s) + 1)]
        cache[0] = 1
        for i in range(1, n + 1):
            if s[i - 1] != '0':
                cache[i] += cache[i - 1]

            if i != 1 and s[i-2:i] < "27" and s[i-2:i] > "09":
                cache[i] += cache[i - 2]
        
        return cache[len(s)]
"""


"""
#Time Limit Exceeded
class Solution:
    def numDecodings(self, s):
        if "0" in s:
            idx = s.index("0")
            if idx == 0 or s[idx-1] == "0" or s[idx-1] > "2":
                return(0)
        
        if len(s) < 1 or s[0] == "0":
            return(0)
        elif len(s) == 1:
            return(1)
        elif len(s) == 2:
            if s < "27" and s != "10" and s != "20":
                return(2)
            else:
                return(1)
        else:
            answer = 0
            if s[0] == "0":
                answer = self.numDecodings(s[1:])
            elif s[0] == "1":
                if s[1] == "0":
                    answer += self.numDecodings(s[2:])
                else:
                    answer += self.numDecodings(s[1:]) + self.numDecodings(s[2:])
            elif s[0] == "2":
                if s[1] == "0":
                    answer += self.numDecodings(s[2:])
                elif s[1] < "7":
                    answer += self.numDecodings(s[1:]) + self.numDecodings(s[2:])
                elif s[1] >= "7":
                    answer += self.numDecodings(s[1:])
            else:
                answer += self.numDecodings(s[1:])
            return(answer)
"""