class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        directions = [[0, 1], [0, -1], [1,0], [-1, 0]]

        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r, c))

            while q:
                a, b = q.popleft()

                for dr, dc in directions:
                    if ((dr+a) < 0 or (dr+a) >= len(grid) or (dc+b) < 0 or (dc+b) >= len(grid[0]) or grid[dr+a][dc+b] == "0"):
                        continue
                    q.append((dr+a, dc+b))
                    grid[dr+a][dc+b] = "0"



        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        return islands