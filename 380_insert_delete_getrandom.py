#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 21:50:53 2019

@author: lz
"""
import random
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
        loc = self.dict.get(val, None)
        
        if loc is None:
            loc = len(self.values)
            
            self.dict[val] = loc
            self.values.append(val)
            
            return(True)
        else:
            return(False)
        
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        loc = self.dict.get(val, None)
        
        if loc is not None:
            temp = self.values[-1]
            
            self.dict[temp] = loc
            del self.dict[val]
            
            self.values[loc] = self.values[-1]
            self.values.pop()
            return(True)
        else:
            return(False)
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return(self.values[random.randrange(len(self.values))])


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
obj.insert(1)
obj.remove(2)
obj.remove(1)
obj.insert(2)
obj.getRandom()
obj.insert(1)
obj.insert(2)
obj.insert(3)
obj.getRandom()