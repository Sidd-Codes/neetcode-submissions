class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1
        for i in t:
            if i in a and a[i] != 0:
                a[i] -= 1
            else:
                return False
        return True;