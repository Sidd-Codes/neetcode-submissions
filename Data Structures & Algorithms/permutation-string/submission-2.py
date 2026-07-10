class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqS1 = {}
        freqS2 = {}
        if len(s2) < len(s1):
            return False
        for i in s1:
            if i not in freqS1:
                freqS1[i] = 0
            freqS1[i] += 1

        for i in range(0, len(s1) - 1):
            if s2[i] not in freqS2:
                freqS2[s2[i]] = 0
            freqS2[s2[i]] += 1
        l = 0
        for r in range(len(s1) - 1, len(s2)):
            if s2[r] not in freqS2:
                freqS2[s2[r]] = 0
            freqS2[s2[r]] += 1            
            if freqS1 == freqS2:
                return True
            freqS2[s2[l]] -= 1
            if freqS2[s2[l]] == 0:
                freqS2.pop(s2[l])
            l += 1
        return False
