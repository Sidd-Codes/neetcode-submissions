class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(vals, path):
            if not vals:
                ans.append(path)
            for i in range(len(vals)):
                dfs(vals[:i] + vals[i+1:], path+[vals[i]])
        dfs(nums, [])
        return ans