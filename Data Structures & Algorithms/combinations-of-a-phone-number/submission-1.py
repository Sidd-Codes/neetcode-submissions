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

        def backtrack(curr, digit):
            if len(curr) == len(digits):
                ans.append(curr)
                return
            for ch in digitsToChar[digits[digit]]:
                curr = curr + ch
                backtrack(curr, digit + 1)
                curr = curr[:-1]
        if digits:
            backtrack("", 0)
        return ans