class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        minPrice = prices[0]
        maxPrice = prices[0]
        for price in prices:
            maxProf = max(maxProf, price - minPrice)
            minPrice = min(price, minPrice)
        return maxProf