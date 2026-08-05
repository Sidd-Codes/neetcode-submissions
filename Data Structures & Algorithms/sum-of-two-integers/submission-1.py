class Solution:
    def getSum(self, a: int, b: int) -> int:
        ans = 0
        carry = 0
        for i in range(32):
            aBit = (a >> i) & 1
            bBit = (b >> i) & 1
            currBit = aBit ^ bBit ^ carry
            carry = (aBit + bBit + carry) > 1
            if currBit:
                ans |= (1 << i)
        if ans > 0x7FFFFFFF:
            ans = ~(ans ^ 0xFFFFFFFF)
        return ans
