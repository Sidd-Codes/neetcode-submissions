class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:
            nextdp = defaultdict(int)
            for total, count in dp.items():
                nextdp[total - num] += count
                nextdp[total + num] += count
            dp = nextdp

        return dp[target]
