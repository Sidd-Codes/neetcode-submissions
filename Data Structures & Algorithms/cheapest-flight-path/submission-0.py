class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        prices = [float("inf")]*n
        for from_i, to_i, price_i in flights:
            adj[from_i].append([to_i, price_i])

        q = deque([(0, src, 0)])

        while q:
            cst, node, stops = q.popleft()
            if stops > k:
                continue
            for d, c in adj[node]:
                if c + cst < prices[d]:
                    prices[d] = c + cst
                    q.append((c + cst, d, stops + 1))
            

        return prices[dst] if prices[dst] != float("inf") else -1


