class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = {}
        for i in hand:
            count[i] = count.get(i, 0) + 1
        
        hand.sort()

        for i in hand:
            if count == {}:
                return True
            if i not in count:
                continue
            count[i] -= 1
            if count[i] == 0:
                del count[i]
            for j in range(i + 1, i + groupSize):
                if j not in count:
                    return False
                count[j] -= 1
                if count[j] == 0:
                    del count[j]
        return True