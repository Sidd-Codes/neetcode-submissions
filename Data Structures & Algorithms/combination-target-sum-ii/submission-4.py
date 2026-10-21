class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def dfs(i, curr, total):
            if total == target:
                ans.append(curr.copy())
                return
            if total > target or i >= len(candidates):
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                elif total + candidates[j] > target:
                    break
                curr.append(candidates[j])
                dfs(j + 1, curr, total + candidates[j])
                curr.pop()
        dfs(0, [], 0)
        return ans               
