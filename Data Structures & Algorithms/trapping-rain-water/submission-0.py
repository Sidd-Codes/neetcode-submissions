class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        maxWater = 0
        leftMax = height[0]
        rightMax = height[-1]

        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                maxWater += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                maxWater += rightMax - height[right]
        return maxWater
