class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        h = []
        ans = []
        for r in range(len(nums)):
            heapq.heappush(h, (-1*nums[r], r))
            if r >= k - 1:
                while l > h[0][1]:
                    heapq.heappop(h)
                ans.append(-1*h[0][0])
                l += 1
        return ans