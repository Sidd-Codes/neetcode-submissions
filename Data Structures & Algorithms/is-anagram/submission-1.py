class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in d1:
                d1[s[i]] = 1
            else:
                d1[s[i]] = d1[s[i]] + 1
            if t[i] not in d2:
                d2[t[i]] = 1
            else:
                d2[t[i]] = d2[t[i]] + 1

        for i in s:
            if i not in d2:
                return False
            if d1[i] != d2[i]:
                return False
        return True