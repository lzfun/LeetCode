#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 19:28:45 2019

@author: ludizhan
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if root.left is None and root.right is None:
            return(1)
        else:
            level = 1
            maximum = root.val
            max_level = 1
            all_node = [root]

            while len(all_node) > 0:
                sums = 0
                num_nodes = len(all_node)
                for node in all_node:
                    if node.left is not None:
                        sums += node.left.val
                        print(node.left.val)
                        if node.left.left is not None or node.left.right is not None:
                            all_node.append(node.left)
                    if node.right is not None:
                        sums += node.right.val
                        print(node.right.val)
                        if node.right.left is not None or node.right.right is not None:
                            all_node.append(node.right)
                del all_node[:num_nodes]
                    
                level += 1
                if sums > maximum:
                    max_level = level
                    maximum = sums

            return(max_level)

head = TreeNode(989)
head.right = TreeNode(10250)
head.right.left = TreeNode(98693)