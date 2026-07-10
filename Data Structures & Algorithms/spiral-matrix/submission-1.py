class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)
        i = top
        j = left
        while top < bottom and left < right:
            # Traverse from left to right
            for j in range(left, right):
                ans.append(matrix[top][j])
            top += 1

            # Traverse downwards
            for i in range(top, bottom):
                ans.append(matrix[i][right - 1])
            right -= 1

            if top < bottom:
                # Traverse from right to left
                for j in range(right - 1, left - 1, -1):
                    ans.append(matrix[bottom - 1][j])
                bottom -= 1

            if left < right:
                # Traverse upwards
                for i in range(bottom - 1, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1
        return ans

