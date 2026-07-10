class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = r

        while l <= r:
            k = (l + r)//2
            total = 0

            for p in piles:
                total += math.ceil(float(p)/k)
            if total <= h:
                ans = k
                r = k - 1
            else:
                l = k + 1
        return ans
