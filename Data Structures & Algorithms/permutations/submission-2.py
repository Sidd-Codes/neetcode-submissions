class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(vals, path):
            if not vals:
                ans.append(path.copy())
            for j in range(len(vals)):
                dfs(vals[:j]+vals[j+1:], path + [vals[j]])
        dfs(nums, [])
        return ans 

        