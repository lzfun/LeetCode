#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 21:56:27 2019

@author: lz
"""

class Solution:
    def invalidTransactions(self, transactions):
        n = len(transactions)
        possible = [False] * n
        
        names = [''] * n
        times = [0] * n
        amounts = [0] * n
        cities = [''] * n
        
        for i, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(',')
            time = int(time)
            amount = int(amount)
            
            names[i] = name
            times[i] = time
            amounts[i] = amount
            cities[i] = city
        
        for i in range(n):
            possible[i] = (amounts[i] > 1000)
            for j in range(n):
                if names[i] == names[j] and cities[i] != cities[j] and abs(times[i] - times[j]) <= 60:
                    possible[i] = True
        
        answer = []
        for i in range(n):
            if possible[i]:
                answer.append(transactions[i])
        return(answer)