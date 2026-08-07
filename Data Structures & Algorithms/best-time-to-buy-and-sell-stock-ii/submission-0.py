class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prevPrice = prices[0]
        profit = 0

        for i in prices[1::]:
            if i > prevPrice:
                profit += i - prevPrice
            prevPrice = i
        return profit