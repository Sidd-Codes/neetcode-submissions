class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0]*numCourses
        ans= []
        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1
        def dfs(node):
            ans.append(node)
            indegree[node] -= 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    dfs(nei)
        for course in range(numCourses):
            if indegree[course] == 0:
                dfs(course)

        

        return ans if len(ans) == numCourses else []

