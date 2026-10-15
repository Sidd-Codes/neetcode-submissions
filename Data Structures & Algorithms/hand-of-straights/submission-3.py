class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        
        for i in hand:
            start = i
            while count[start]:
                start -= 1
            while start <= i:
                while count[start]:
                    for j in range(start, start + groupSize):
                        if not count[j]:
                            return False
                        count[j] -= 1
                start += 1
        return True