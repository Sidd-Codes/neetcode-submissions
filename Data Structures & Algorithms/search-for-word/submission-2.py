class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        directions = [[0 , 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(row, col, i):
            if i == len(word):
                return True
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or board[row][col] != word[i] or board[row][col] == '#':
                return False
            temp = board[row][col]
            board[row][col] = '#'
            ans = dfs(row + 1, col, i + 1) or dfs(row, col + 1, i + 1) or dfs(row - 1, col, i + 1) or dfs(row, col - 1, i + 1)
            board[row][col] = temp
            return ans

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False
