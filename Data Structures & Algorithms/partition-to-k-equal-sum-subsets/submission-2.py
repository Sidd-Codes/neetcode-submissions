class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        if total%k != 0:
            return False
        target = total // k
        nums.sort(reverse = True)

        if nums[0] > target:
            return False
        
        subsets = [0] * k

        def backtrack(i):
            if i == len(nums):
                return True
            for j in range(k):
                if nums[i] + subsets[j] <= target:
                    subsets[j] += nums[i]

                    if backtrack(i+1):
                        return True
                    subsets[j] -= nums[i]
                if subsets[j] == 0:
                    break
            return False
        return backtrack(0)