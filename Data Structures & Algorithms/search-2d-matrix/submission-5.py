class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) * len(matrix[0]) - 1


        while left <= right:
            mid = (left + right) // 2
            midX = mid // len(matrix[0])
            midY = mid % len(matrix[0])
            if matrix[midX][midY] == target:
                return True
            if matrix[midX][midY] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False