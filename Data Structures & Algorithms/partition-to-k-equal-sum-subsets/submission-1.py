class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        totalSum = sum(nums)
        if totalSum % k != 0:
            return False
        partSum = totalSum  // k
        if nums[0] > partSum:
            return False
        parts = [0]*k

        def dfs(i):
            if i == len(nums):
                return True
            for part in range(k):
                if parts[part] + nums[i] <= partSum:
                    parts[part] += nums[i]
                    if dfs(i + 1):
                        return True
                    parts[part] -= nums[i]
                
                if parts[part] == 0:
                    break

            return False


        return dfs(0)

