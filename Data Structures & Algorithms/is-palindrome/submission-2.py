class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while left < right:
            while left < right and not ((ord('A') <= ord(s[left]) <= ord('Z')) or (ord('a') <= ord(s[left]) <= ord('z')) or (ord('0') <= ord(s[left]) <= ord('9'))):
                left += 1
            while left < right and not ((ord('A') <= ord(s[right]) <= ord('Z')) or (ord('a') <= ord(s[right]) <= ord('z')) or (ord('0') <= ord(s[right]) <= ord('9'))):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True