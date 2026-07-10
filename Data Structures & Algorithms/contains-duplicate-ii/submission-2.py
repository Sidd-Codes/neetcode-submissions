class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dictNums = {}

        for i in range(len(nums)):
            if nums[i] in dictNums:
                if i - dictNums[nums[i]] <= k:
                    return True
            dictNums[nums[i]] = i
        return False