class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if nums[0] >= target:
            return 1

        i = 0
        total = 0
        minLen = float("inf")

        for j in range(len(nums)):
            total += nums[j]
            while total >= target:
                minLen = min(minLen, j - i + 1)
                total -= nums[i]
                i += 1

        return 0 if minLen == float("inf") else minLen