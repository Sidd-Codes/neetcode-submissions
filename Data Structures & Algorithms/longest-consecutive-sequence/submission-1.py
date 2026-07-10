class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        maxLength = 0
        for i in nums:
            if i-1 not in n:
                currLength = 1
                while i + currLength in n:
                    currLength += 1
                maxLength = max(maxLength, currLength)
        return maxLength