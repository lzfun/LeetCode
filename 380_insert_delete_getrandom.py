#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 21:50:53 2019

@author: lz
"""
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = []
        self.dict = {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.values:
            return(False)
        else:
            loc = len(self.values)
            self.values.append(val)
            return(True)
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.values:
            return(True)
        else:
            return(False)
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()