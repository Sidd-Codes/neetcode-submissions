class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = []
        for i in tokens:
            if i == '+':
                val1 = ans.pop()
                val2 = ans.pop()
                ans.append(val1 + val2)
            elif i == '-':
                val1 = ans.pop()
                val2 = ans.pop()
                ans.append(val2 - val1)
            elif i == '*':
                val1 = ans.pop()
                val2 = ans.pop()
                ans.append(val1 * val2)
            elif i == '/':
                val1 = ans.pop()
                val2 = ans.pop()
                ans.append(int(float(val2) / val1))
            else:
                ans.append(int(i))
        return ans.pop()
                