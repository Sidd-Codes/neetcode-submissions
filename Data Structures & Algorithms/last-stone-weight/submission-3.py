class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            st1 = heapq.heappop(stones)
            st2 = heapq.heappop(stones)
            if st1 != st2:
                if st2 > st1:
                    heapq.heappush(stones, st1 - st2)
        stones.append(0)
        return abs(stones[0])
