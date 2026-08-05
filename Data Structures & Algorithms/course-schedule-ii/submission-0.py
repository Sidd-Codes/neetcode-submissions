class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for course, pre in prerequisites:
            adj[course].append(pre)

        ans = []
        visited = set()
        cycle = set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)

            for pre in adj[course]:
                if dfs(pre) == False:
                    return False
            visited.add(course)
            cycle.remove(course)
            ans.append(course)

        for course in range(numCourses):
            if dfs(course) == False:
                return []

        return ans