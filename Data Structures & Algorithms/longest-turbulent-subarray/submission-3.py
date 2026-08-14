class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        maxLen = 0
        currLen = 0
        sign = -1
        for n in range(len(arr) - 1):
            curr = arr[n]
            nex = arr[n+1]
            if curr < nex:
                currLen = currLen + 1 if sign == 1 else 1
                sign = 0
            elif curr > nex:
                currLen = currLen + 1 if sign == 0 else 1
                sign = 1
            else:
                currLen = 0
                sign = -1
            maxLen = max(maxLen, currLen)
        return maxLen + 1