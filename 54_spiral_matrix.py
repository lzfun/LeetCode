#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 00:04:55 2019

@author: lz
"""

class Solution:
    def spiralOrder(self, matrix):
        # m: number of column, n: number of row
        m, n = len(matrix), len(matrix[0])
        min_i = 1
        min_j = 0
        max_i = m - 1
        max_j = n - 1
        i = j = 0
        answer = [matrix[i][j]]
        
        print("min_i, max_i: {}, {}; min_j, max_j: {}, {}".format(min_i, max_i, min_j, max_j))
        while (min_i <= max_i) or (min_j <= max_j):
            for j in range(j+1, max_j + 1):
                answer.append(matrix[i][j])
            max_j -= 1
            print("min_i, max_i: {}, {}; min_j, max_j: {}, {}".format(min_i, max_i, min_j, max_j))
            for i in range(i+1, max_i + 1):
                answer.append(matrix[i][j])
            max_i -= 1
            print("min_i, max_i: {}, {}; min_j, max_j: {}, {}".format(min_i, max_i, min_j, max_j))
            for j in range(j-1, min_j-1, -1):
                answer.append(matrix[i][j])
            min_j += 1
            print("min_i, max_i: {}, {}; min_j, max_j: {}, {}".format(min_i, max_i, min_j, max_j))
            for i in range(i-1, min_i-1, -1):
                answer.append(matrix[i][j])
            min_i += 1
            print("min_i, max_i: {}, {}; min_j, max_j: {}, {}".format(min_i, max_i, min_j, max_j))
        return(answer)