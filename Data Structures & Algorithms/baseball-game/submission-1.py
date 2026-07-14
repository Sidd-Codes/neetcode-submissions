class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        total = 0
        for curr in operations:
            if curr == "C":
                ans.pop()
            elif curr == "D":
                newNum = ans[-1] * 2
                ans.append(newNum)
            elif curr == "+":
                num1 = ans[-1]
                num2 = ans[-2]
                ans.append(num1 + num2)
            else:
                ans.append(int(curr))
        while ans:
            total += ans.pop()
        return total