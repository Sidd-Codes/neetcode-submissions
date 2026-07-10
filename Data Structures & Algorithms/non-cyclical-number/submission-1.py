class Solution:
    def isHappy(self, n: int) -> bool:
        total = 0
        curr = n
        totalSet = set()
        while total != 1:
            total = 0
            while curr > 0:
                total += (curr % 10)**2
                curr //= 10
            if total in totalSet:
                return False
            totalSet.add(total)
            curr = total
        return True
