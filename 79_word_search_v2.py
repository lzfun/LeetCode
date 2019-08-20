"""
lz@2019/08/17
Similar DFS idea, improved Version
"""

import copy
class Solution:
    def exist(self, board, word):
        if len(word) < 1:
            return(False)
        m, n= len(board), len(board[0])
		
		visited = [[0]*n]*m

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.existSubstr(board, substr, i, j, m, n, visited):
						return(True)
        return(False)

    def existSubstr(self, board, substr, i, j, m, n, visited):
        if len(substr) <= 0:
            return(True)
			
		if i < 0 or j < 0 or i >= m or j >= n:
			return(False)
		
		if visited[i][j]:
			return(False)
			
		if board[i][j] != substr[0]:
			return(False)
		
		visited[i][j] = 1
		if self.existSubstr(board, substr[1:], i - 1, j, m, n, visited) or self.existSubstr(board, substr[1:], i, j - 1, m, n, visited) or self.existSubstr(board, substr[1:], i + 1, j, m, n, visited) or self.existSubstr(board, substr[1:], i, j + 1, m, n, visited):
			return(True)
		
		visited[i][j] = 0
		return(False)
