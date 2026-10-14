class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        visited = set()
        for ui, vi, ti in times:
            edges[ui].append((vi, ti))

        minHeap = []
        heapq.heappush(minHeap, (0, k))
        t = 0
        while minHeap:
            t1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            t = t1
            for n2, t2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (t2 + t1, n2))
        return t if len(visited) == n else -1