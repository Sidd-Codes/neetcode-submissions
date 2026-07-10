class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        found = {}
        maxLen = 0
        initial = 0
        curr = 0
        i = 0
        while i < len(s):
            if s[i] in found:
                initial += 1
                i = initial
                if curr > maxLen:
                    maxLen = curr
                curr = 0
                found = {}
            else:
                found[s[i]] = 0
                curr += 1
                i += 1
        if curr > maxLen:
            maxLen = curr
        return maxLen
