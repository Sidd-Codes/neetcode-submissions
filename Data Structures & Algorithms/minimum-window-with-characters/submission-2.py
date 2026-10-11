class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = defaultdict(int)
        for a in t:
            tMap[a] += 1
        sMap = defaultdict(int)
        ans = ""
        have = 0
        l = 0
        minLen = float('inf')
        for r in range(len(s)):
            if s[r] in tMap:
                sMap[s[r]] += 1
                if sMap[s[r]] == tMap[s[r]]:
                    have += 1
            while have == len(tMap):
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    ans = s[l:r + 1]
                if s[l] in tMap:
                    if sMap[s[l]] == tMap[s[l]]:
                        have -= 1
                    sMap[s[l]] -= 1
                l += 1
        return ans