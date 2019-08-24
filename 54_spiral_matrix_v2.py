#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 16:04:55 2019

@author: lz
"""

class Solution:
    def spiralOrder(self, matrix):
        # m: number of column, n: number of row
        if not matrix:
            return([])
            
        m, n = len(matrix), len(matrix[0])
        min_i = 0
        min_j = 0
        max_i = m - 1
        max_j = n - 1
        
        answer = []
        
        while min_i <= max_i and min_j <= max_j:
            for item in self.spiralCoords(matrix, min_i, min_j, max_i, max_j):
                answer.append(item)
            min_i += 1
            max_i -= 1
            min_j += 1
            max_j -= 1
        return(answer)

    
    def spiralCoords(self, matrix, min_i, min_j, max_i, max_j):
        for j in range(min_j, max_j + 1):
            yield matrix[min_i][j]
        for i in range(min_i + 1, max_i + 1):
            yield matrix[i][max_j]
        if min_i < max_i and min_j < max_j:
            for j in range(max_j - 1, min_j - 1, -1):
                yield matrix[max_i][j]
            for i in range(max_i - 1, min_i, -1):
                yield matrix[i][min_j]
