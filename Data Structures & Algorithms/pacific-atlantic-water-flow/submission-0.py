class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if heights is None:
            return None
        ans = []
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        atl = set()
        pac = set()
        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or r < 0 or c < 0  or r >= len(heights) or c >= len(heights[0]) or heights[r][c] < prevHeight):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for r in range(len(heights)):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, len(heights[0]) - 1, atl, heights[r][len(heights[0]) - 1])

        for c in range(len(heights[0])):
            dfs(0, c, pac, heights[0][c])
            dfs(len(heights) - 1, c, atl, heights[len(heights) - 1][c])

        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r, c) in atl and (r, c) in pac:
                    ans.append([r, c])
        return ans

