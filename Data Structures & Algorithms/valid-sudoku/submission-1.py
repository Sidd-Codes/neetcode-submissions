class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = defaultdict(set)
        rows = defaultdict(set)
        cols = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                digit = board[i][j]
                if digit != ".":
                    if digit in rows[i]:
                        return False
                    rows[i].add(digit)
                    if digit in cols[j]:
                        return False
                    cols[j].add(digit)
                    if digit in squares[(i//3, j//3)]:
                        return False
                    squares[(i//3, j//3)].add(digit)
        return True