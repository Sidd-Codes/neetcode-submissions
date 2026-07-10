class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        found = {}
        l = 0
        maxSubstring = 0
        for r in range(len(s)):
            if s[r] in found:
                l = max(found[s[r]] + 1, l)
            found[s[r]] = r
            maxSubstring = max(maxSubstring, r - l + 1)
        return maxSubstring