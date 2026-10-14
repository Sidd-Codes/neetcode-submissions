class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        currSum = 0
        for i in range(len(nums)):
            currSum = max(currSum + nums[i], nums[i])
            ans = max(ans, currSum)
        return ans