class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        ans = 0
        visited = [False]*(n)
        def dfs(node):
            for nei in adj[node]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)

        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                ans += 1
            
        return ans