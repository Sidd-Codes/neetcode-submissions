class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        while l < r:
            mid = (l + r) // 2
            numDays = 1
            curr = 0
            for w in weights:
                if curr + w > mid:
                    numDays += 1
                    curr = 0
                    if numDays > days:
                        l = mid + 1
                        break
                curr += w
            if numDays <= days:
                r = mid
        return l
