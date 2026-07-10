class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = right
        while left <= right:
            mid = (left + right)//2
            totalTime = 0

            for i in piles:
                totalTime += math.ceil(float(i) / mid)
            if totalTime <= h:
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        return ans