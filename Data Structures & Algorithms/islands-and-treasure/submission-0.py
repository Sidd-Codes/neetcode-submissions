class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        dist = 0
        q = deque()
        visited = set()

        def addCell(r, c):
            if r < 0 or c < 0 or r == len(grid) or c == len(grid[0]) or grid[r][c] == -1 or (r, c) in visited:
                return
            visited.add((r, c))
            q.append([r, c])


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1
