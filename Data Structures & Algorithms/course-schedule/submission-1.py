class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegree = [0]*numCourses
        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1
        q = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        while q:
            pre = q.popleft()
            for course in adj[pre]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)

        for course in range(numCourses):
            if indegree[course] != 0:
                return False
        return True
