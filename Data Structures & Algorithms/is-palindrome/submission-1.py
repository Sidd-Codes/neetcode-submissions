class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = []
        for i in s:
            if ('A' <= i <= 'Z'):
                a.append(chr(ord(i) + 32))
            elif ('a' <= i <= 'z') or ('0' <= i <= '9'):
                a.append(i)
        print(a)
        if s is None or len(s) <=1:
            return True
        i = 0
        j = len(a)-1
        while i < j:
            if a[i] != a[j]:
                return False
            i += 1
            j -= 1
        return True