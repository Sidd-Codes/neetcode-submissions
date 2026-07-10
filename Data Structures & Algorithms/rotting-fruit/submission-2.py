class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = {}
        q = deque()
        fresh = 0
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j, 0))
        if fresh == 0:
            return 0
        while q:
            x, y, time = q.popleft()
            for dx, dy in directions:
                if x + dx < 0 or x + dx >= len(grid) or y + dy < 0 or y + dy >= len(grid[0]) or grid[x + dx][y + dy] != 1:
                    continue
                fresh -= 1
                if fresh == 0:
                    return time + 1
                grid[x + dx][y + dy] = 2
                q.append((x + dx, y + dy, time + 1))
        return -1