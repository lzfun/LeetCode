"""
lz@2019/08/17
Time Limit Exceeded
"""

import copy
class Solution:
    def exist(self, board, word):
        if len(word) < 1:
            return(False)
        m = len(board)
        n = len(board[0])
        result = False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    subboard = copy.deepcopy(board)
                    subboard[i][j] = ' '
                    answer = self.existSubstr(subboard, word[1:], i, j, m, n)
                    if answer:
                        result = True
        return(result)

    def existSubstr(self, board, substr, s_i, s_j, m, n):
        if len(substr) <= 0:
            return(True)
        elif len(substr) == 1:
            if substr in self.neighbor(board, s_i, s_j, m, n):
                return(True)
            else:
                return(False)
        else:
            neighbors = self.neighbor(board, s_i, s_j, m, n)
            if substr[0] in neighbors:
                answer = False
                for loc_i, loc_j in neighbors[substr[0]]:
                    subboard = copy.deepcopy(board)
                    subboard[loc_i][loc_j] = ' '
                    result = self.existSubstr(subboard, substr[1:], loc_i, loc_j, m, n)
                    if result:
                        answer = True
            else:
                return(False)
        return(answer)

    def neighbor(self, board, i, j, m, n):
        answer = {}
        if i > 0:
            key = board[i-1][j]
            answer[key] = [(i-1, j)]
        if j > 0:
            key = board[i][j-1]
            if key not in answer:
                answer[key] = [(i, j-1)]
            else:
                answer[key].append((i, j-1))
        if i < (m - 1):
            key = board[i+1][j]
            if key not in answer:
                answer[key] = [(i + 1, j)]
            else:
                answer[key].append((i + 1, j))
        if j < n - 1:
            key = board[i][j+1]
            if key not in answer:
                answer[key] = [(i, j + 1)]
            else:
                answer[key].append((i, j + 1))
        return(answer)


