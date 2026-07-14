class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        total = 0
        for curr in operations:
            if curr == "C":
                total -= ans.pop()
                continue
            elif curr == "D":
                total += (ans[-1] * 2)
                ans.append(ans[-1] * 2)
                continue
            elif curr == "+":
                total += (ans[-1] + ans[-2])
                ans.append(ans[-1] + ans[-2])
                continue
            else:
                ans.append(int(curr))
                total += int(curr)
        return total