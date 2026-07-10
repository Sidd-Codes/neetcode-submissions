class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ans = 0
        adj = [[] for _ in range(n)]
        visit = [False] * n
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        def dfs(node):
            for nei in adj[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)

        for i in range(n):
            if not visit[i]:
                visit[i] = True
                dfs(i)
                ans += 1
        return ans