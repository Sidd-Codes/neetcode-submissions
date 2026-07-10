class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        cols = set()
        diag1 = set()
        diag2 = set()

        board = [-1]*n
        ans = []

        def dfs(r):
            if r == n:
                curr = []
                for i in board:
                    curr.append("."*i + "Q" + "."*(n - i - 1))
                ans.append(curr)
                return
            for c in range(n):
                if c in cols or r + c in diag1 or r - c in diag2:
                    continue
                
                cols.add(c)
                diag1.add(r + c)
                diag2.add(r - c)
                board[r] = c

                dfs(r + 1)

                cols.remove(c)
                diag1.remove(r + c)
                diag2.remove(r - c)
        dfs(0)
        return ans