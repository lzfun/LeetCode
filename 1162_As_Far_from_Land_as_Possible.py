#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 20:56:08 2019

@author: lz
"""

import copy
class Solution:
    def maxDistance(self, grid):
        if len(grid) < 1 or len(grid[0]) < 1:
            return(-1)
        m = len(grid)
        n = len(grid[0])
        disGrid = copy.deepcopy(grid)
        land = []
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    disGrid[i][j] = -1
                    land.append((i, j))
                    
        for landi, landj in land:
            updated = copy.deepcopy(disGrid)
            updated[landi][landj] = 'Y'
            self.updateDis(disGrid, landi, landj, m, n, 0, updated)

        maximum = 0
        for i in range(m):
            for j in range(n):
                maximum = max(maximum, grid[i][j])
        return(maximum)
    
    def updateDis(self, disGrid, i, j, m, n, distance, updated):
        if i >= 0 and j >= 0 and i < m and j < n:
            if i > 0 and updated[i-1][j] != 'Y':
                if disGrid[i-1][j] == 0:
                    disGrid[i-1][j] = distance + 1
                elif disGrid[i-1][j] > 0:
                    disGrid[i-1][j] = min(disGrid[i-1][j], distance + 1)
                updated[i-1][j] = 'Y'

            if j > 0 and updated[i][j-1] != 'Y':
                if disGrid[i][j-1] == 0:
                    disGrid[i][j-1] = distance + 1
                elif disGrid[i][j-1] > 0:
                    disGrid[i][j-1] = min(disGrid[i][j-1], distance + 1)
                updated[i][j-1] = 'Y'

            if i < m - 1 and updated[i+1][j] != 'Y':
                if disGrid[i+1][j] == 0:
                    disGrid[i+1][j] = distance + 1
                elif disGrid[i+1][j] > 0:
                    disGrid[i+1][j] = min(disGrid[i+1][j], distance + 1)
                updated[i+1][j] = 'Y'

            if j < n - 1 and updated[i][j+1] != 'Y':
                if disGrid[i][j+1] == 0:
                    disGrid[i][j+1] = distance + 1
                elif disGrid[i][j+1] > 0:
                    disGrid[i][j+1] = min(disGrid[i][j+1], distance + 1)
                updated[i][j+1] = 'Y'

            self.updateDis(disGrid, i-1, j, m, n, distance+1, updated)
            self.updateDis(disGrid, i, j-1, m, n, distance+1, updated)
            self.updateDis(disGrid, i+1, j, m, n, distance+1, updated)
            self.updateDis(disGrid, i, j+1, m, n, distance+1, updated)
        