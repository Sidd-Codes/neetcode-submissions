class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >  n-1:
            return False

        visited = set()
        adj = [[] for _ in range(n)]
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        def dfs(node, par):
            if node in visited:
                return False
            visited.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n
