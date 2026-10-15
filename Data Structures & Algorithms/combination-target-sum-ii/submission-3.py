class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def dfs(i, curr, total):
            if total == target:
                ans.append(curr.copy())
                return
            elif total > target or i >= len(candidates):
                return
            
            curr.append(candidates[i])
            dfs(i + 1, curr, total + candidates[i])
            curr.pop()

            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            
            dfs(i + 1, curr, total)
        
        dfs(0, [], 0)
        return ans