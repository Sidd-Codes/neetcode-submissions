class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []

        digitsToChar = { "2" : "abc",
                         "3" : "def",
                         "4" : "ghi",
                         "5" : "jkl",
                         "6" : "mno",
                         "7" : "pqrs",
                         "8" : "tuv",
                         "9" : "wxyz" }
        
        def backtrack(i, s):
            if len(s) == len(digits):
                ans.append(s)
                return
            for d in digitsToChar[digits[i]]:
                backtrack(i + 1, s + d)
        if digits:
            backtrack(0, "")

        return ans