class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        currSub = set()
        lenSub = 0
        ans = []
        for i in s:
            lenSub += 1
            count[i] -= 1
            if count[i] == 0:
                if i in currSub:
                    currSub.remove(i)
                if len(currSub) == 0:
                    ans.append(lenSub)
                    lenSub = 0
            elif i not in currSub:
                currSub.add(i)
        return ans
