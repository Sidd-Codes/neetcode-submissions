class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
             return False
        
        i = 0
        j = len(s1) - 1
        s1Map = defaultdict(int)
        s2Map = defaultdict(int)
        
        for i in range(len(s1)):
            s1Map[s1[i]] += 1
            s2Map[s2[i]] += 1
        i = 0
        while j < len(s2) - 1 and s1Map != s2Map:
            s2Map[s2[i]] -= 1
            if s2Map[s2[i]] == 0:
                del s2Map[s2[i]]
            i += 1
            j += 1
            s2Map[s2[j]] += 1

        if s1Map == s2Map:
            return True
        return False