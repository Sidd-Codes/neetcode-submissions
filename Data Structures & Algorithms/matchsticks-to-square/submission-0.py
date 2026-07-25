class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        perimeter = sum(matchsticks)

        if perimeter % 4 != 0:
            return False
        sideTotal = perimeter // 4
        matchsticks.sort(reverse = True)
        sides = [0]*4

        def dfs(i):
            if i == len(matchsticks):
                return True

            for side in range(4):
                if sides[side] + matchsticks[i] <= sideTotal:
                    sides[side] += matchsticks[i]
                    if dfs(i + 1):
                        return True
                    sides[side] -= matchsticks[i]

                
            return False

        return dfs(0)            