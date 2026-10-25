class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        part = []
        def dfs(i):
            if i == len(s):
                ans.append(part.copy())
                return
            for j in range(i, len(s)):
                if isPali(s[i:j + 1]):
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()
        def isPali(st):
            l = 0
            r = len(st) - 1
            while l < r:
                if st[l] != st[r]:
                    return False
                l += 1
                r -= 1
            return True
        dfs(0)
        return ans