class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        found = set()
        found.add(s[0])
        i = 0
        maxLen = 0

        for j in range(1, len(s)):
            if s[j] in found:
                while s[j] in found:
                    found.remove(s[i])
                    i += 1
            found.add(s[j])
            maxLen = max(maxLen, j - i + 1)
        return maxLen