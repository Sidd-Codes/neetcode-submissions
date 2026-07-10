class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = {}
        countT = {}

        for i in t:
            countT[i] = 1 + countT.get(i, 0)
        ans = ""
        have = 0
        need = len(countT)
        l = 0
        minWindow = float('inf')

        for r in range(len(s)):
            
            window[s[r]] = 1 + window.get(s[r], 0)
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1

            while have == need:
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    if r - l + 1 < minWindow:
                        ans = s[l:r+1]
                        minWindow = r - l + 1
                    have -= 1
                l += 1
        return ans              