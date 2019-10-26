#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:49:51 2019

@author: lz
"""

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.count = 0

    def addNum(self, num: int) -> None:
        if self.count < 1:
            self.nums.append(num)
        else:
            # use binary search to find the index to insert
            l, r = 0, self.count - 1
            while l < r:
                middle = (l + r)//2
                if num > self.nums[middle]:
                    l = middle + 1
                elif num < self.nums[middle]:
                    r = middle - 1
                else:
                    l = r = middle
                    
            if num > self.nums[l]:
                self.nums.insert(l+1, num)
            else:
                self.nums.insert(l, num)
        
        self.count += 1

    def findMedian(self) -> float:
        if self.count % 2 == 0:
            return((self.nums[self.count // 2] + self.nums[self.count // 2 - 1])/2.0)
        else:
            return(self.nums[self.count // 2])