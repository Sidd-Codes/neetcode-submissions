class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]

        currMax = 1
        currMin = 1

        for num in nums:
            currMax, currMin = max(num, currMax*num, currMin*num), min(num, currMax*num, currMin*num)
            ans = max(ans, currMax)
        return ans
