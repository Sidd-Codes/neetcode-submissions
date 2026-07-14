class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        total = 0
        for curr in operations:
            if curr == "C":
                ans.pop()
                continue
            elif curr == "D":
                newNum = ans[-1] * 2
                ans.append(newNum)
                continue
            elif curr == "+":
                num1 = ans[-1]
                num2 = ans[-2]
                ans.append(num1 + num2)
                continue
            else:
                ans.append(int(curr))
        while ans:
            total += ans.pop()
        return total