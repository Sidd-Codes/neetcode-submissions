class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[False] * numCourses for _ in range(numCourses)]
        ans = []
        for a, b in prerequisites:
            adj[a][b] = True
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    adj[i][j] = adj[i][j] or (adj[i][k] and adj[k][j])
        
        for a, b in queries:
            ans.append(adj[a][b])
        return ans