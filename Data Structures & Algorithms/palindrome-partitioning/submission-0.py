class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans, part = [], []

        def dfs(i):
            if i >= len(s):
                ans.append(part.copy())
                return
            for j in range(i, len(s)):
                if isPali(s[i : j + 1]):
                    part.append(s[i : j + 1])
                    dfs(j + 1)
                    part.pop()
        

        def isPali(s):
            i = 0
            j = len(s) - 1

            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1

            return True

        dfs(0)
        return ans