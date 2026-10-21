class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        def dfs(i, curr, total):
            if i >= len(nums) or total > target:
                return
            elif total == target:
                ans.append(curr.copy())
                return
            for j in range(i, len(nums)):
                if nums[j] + total > target:
                    break
                curr.append(nums[j])
                dfs(j, curr, total + nums[j])
                curr.pop()

        dfs(0, [], 0)
        return ans 