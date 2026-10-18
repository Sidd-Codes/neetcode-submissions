class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stack = [(temperatures[0], 0)]
        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                t, ind = stack.pop()
                ans[ind] = i - ind
            stack.append((temperatures[i], i))
        return ans