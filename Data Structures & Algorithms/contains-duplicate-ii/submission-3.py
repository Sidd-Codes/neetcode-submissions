class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dictNums = {}

        for i in range(len(nums) - 1):
            for j in range(i + 1, min(len(nums), i + k + 1)):
                if nums[i] == nums[j]:
                    return True
        return False