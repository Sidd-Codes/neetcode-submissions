class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False]*len(s) for _ in range(len(s))]
        maxLen = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i - 1 <= 1 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if(j - i + 1 > maxLen):
                        maxLen = j - i + 1
                        maxInd = i

        return s[maxInd:maxInd + maxLen]