class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            dic[course].append(pre)
        visiting = set()
        def dfs(course):
            if course in visiting:
                return False
            if dic[course] == []:
                return True
            visiting.add(course)
            for p in dic[course]:
                if not dfs(p):
                    return False
            visiting.remove(course)
            dic[course] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True