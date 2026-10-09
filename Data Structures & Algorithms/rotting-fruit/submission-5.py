class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        count = 0
        for i in range(len(grid)):
            for j in range((len(grid[0]))):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    count += 1
        if count == 0:
            return 0
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        time = 0
        while q:
            time += 1
            for i in range(len(q)):
                x, y = q.popleft()
                for dx, dy in directions:
                    if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and grid[x+dx][y+dy] == 1:
                        count -= 1
                        if count == 0:
                            return time
                        grid[x+dx][y+dy] = 2
                        q.append((x + dx, y + dy))

        return -1
            