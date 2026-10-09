class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j))
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        level = 0
        while q:
            level += 1
            for i in range(len(q)):
                a, b = q.popleft()
                for dx, dy in directions:
                    if a + dx >= len(grid) or a + dx < 0 or b + dy >= len(grid[0]) or b + dy < 0 or (a + dx, b + dy) in visited:
                        continue
                    if grid[a + dx][b + dy] > 0:
                        visited.add((a + dx, b + dy))
                        q.append((a + dx, b + dy))
                        grid[a + dx][b + dy] = level
        
                        

            