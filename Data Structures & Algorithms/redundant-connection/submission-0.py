class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0]*(len(edges) + 1)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
        
        q = deque()
        
        for i in range(1, len(edges) + 1):
            if indegree[i] == 1:
                q.append(i)

        while q:
            vertex = q.popleft()
            indegree[vertex] -= 1
            for vert in adj[vertex]:
                indegree[vert] -= 1
                if indegree[vert] == 1:
                    q.append(vert)
        
        for u, v in reversed(edges):
            if indegree[u] == 2 and indegree[v]:
                return [u, v]
        return []