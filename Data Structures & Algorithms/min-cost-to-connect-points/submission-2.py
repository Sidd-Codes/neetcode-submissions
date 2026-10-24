class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        node = 0
        dist = [100000000]*len(points)
        edges =0
        ans = 0
        visit = [False]*len(points)

        while edges < len(points) - 1:
            nextNode = -1
            visit[node] = True
            for i in range(len(points)):
                if visit[i]:
                    continue
                curr = abs(points[i][0] - points[node][0]) + abs(points[i][1] - points[node][1])

                dist[i] = min(dist[i], curr)
                if nextNode == -1 or dist[i] < dist[nextNode]:
                    nextNode = i
            ans += dist[nextNode]
            node = nextNode
            edges += 1
        return ans
