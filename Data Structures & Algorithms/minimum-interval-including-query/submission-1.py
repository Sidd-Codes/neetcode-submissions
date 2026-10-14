class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        h = []
        i = 0
        intervals.sort()
        ans = {}
        for q in sorted(queries):
            while i < len(intervals) and q >= intervals[i][0]:
                heapq.heappush(h, ((intervals[i][1] - intervals[i][0] + 1), intervals[i][1]))
                i += 1
            while h and h[0][1] < q:
                heapq.heappop(h)
            ans[q] = h[0][0] if h else -1
        return [ans[q] for q in queries]