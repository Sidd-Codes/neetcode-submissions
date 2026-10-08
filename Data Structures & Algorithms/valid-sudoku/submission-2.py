class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowNums = [0]*9
        colNums = [0]*9
        boxNums = [0]*9

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                val = int(board[r][c]) - 1

                if (1 << val) & rowNums[r]:
                    return False
                if (1 << val) & colNums[c]:
                    return False
                if (1 << val) & boxNums[(r//3)*3 + (c//3)]:
                    return False

                rowNums[r] |= (1 << val)
                colNums[c] |= (1 << val)
                boxNums[(r//3)*3 + (c//3)] |= (1 << val)

        return True
            
