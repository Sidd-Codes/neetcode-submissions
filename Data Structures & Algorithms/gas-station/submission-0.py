class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        idx = 0
        total = 0
        if sum(gas) < sum(cost):
            return -1
        for i in range(len(gas)):
            total += gas[i]
            if cost[i] > total:
                idx = i + 1
                total = 0
            else:
                total -= cost[i]
        return idx