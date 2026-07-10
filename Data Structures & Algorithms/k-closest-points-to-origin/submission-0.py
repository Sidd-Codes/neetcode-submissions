class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        ans = []
        for i in points:
            dist = i[0]**2 + i[1]**2
            heapq.heappush(maxHeap, [-dist, i])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        for i in maxHeap:
            ans.append(i[1])
        return ans
