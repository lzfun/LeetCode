#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 22:58:15 2019

@author: lz
"""

class Solution(object):
    def kConcatenationMaxSum(self, A, K):
        def kadane(A):
            ans = bns = 0
            for x in A:
                bns += x
                if x > bns: bns = x
                if bns > ans: ans = bns
            return ans
        
        MOD = 10**9 + 7


        if K <= 2:
            return kadane(A) %MOD if K == 1 else kadane(A+A) %MOD
        
        S = sum(A)
        if S <= 0:
            return max(kadane(A), kadane(A+A)) % MOD
        base = S * (K-2) % MOD
        
        prefix = suffix = 0
        su = 0
        for x in A:
            su += x
            if su > prefix: prefix = su
        su = 0
        for x in reversed(A):
            su += x
            if su > suffix: suffix = su
        return (base + prefix + suffix) % MOD