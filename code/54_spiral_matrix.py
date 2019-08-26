#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 00:04:55 2019

@author: lz
"""

class Solution:
    def spiralOrder(self, matrix):
        # m: number of column, n: number of row
        if len(matrix) < 1 or len(matrix[0]) < 1:
            return([])
        m, n = len(matrix), len(matrix[0])
        min_i = 1
        min_j = 0
        max_i = m - 1
        max_j = n - 1
        i = j = 0
        answer = [matrix[i][j]]
        
        if n == 1:
            for i in range(1, max_i + 1):
                answer.append(matrix[i][j])
            return(answer)
        
        stop = False
        while not stop:
            if j + 1 > max_j:
                stop = True
            elif not stop:
                for j in range(j + 1, max_j + 1):
                    answer.append(matrix[i][j])
                max_j -= 1
            
            if i + 1 > max_i:
                stop = True
            elif not stop:
                for i in range(i + 1, max_i + 1):
                    answer.append(matrix[i][j])
                max_i -= 1
            
            if j - 1 < min_j:
                stop = True
            elif not stop:
                for j in range(j - 1, min_j - 1, -1):
                    answer.append(matrix[i][j])
                min_j += 1
            
            if i - 1 < min_i:
                stop = True
            elif not stop:
                for i in range(i - 1, min_i - 1, -1):
                    answer.append(matrix[i][j])
                min_i += 1
        return(answer)