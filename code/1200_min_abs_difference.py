#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 22:11:07 2019

@author: lz
"""

def minimumAbsDifference(arr):
    arr.sort()
    answer = []
    current_min = arr[1] - arr[0]
    for i in range(1, len(arr)):
        local_min = arr[i] - arr[i-1]
        if local_min < current_min:
            answer = [[arr[i-1], arr[i]]]
        elif local_min == current_min:
            answer.append([arr[i-1], arr[i]])
    return(answer)