class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        curr = 0
        found = {}
        for i in nums:
            found[i] = 0
        for i in range(len(nums)+1):
            if i not in found:
                return i        