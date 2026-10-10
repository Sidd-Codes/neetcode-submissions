class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= k:
            return len(s)
        ans = 0
        i = 0
        maxFreq = 0
        freq = defaultdict(int)
        for j in range(len(s)):
            freq[s[j]] += 1
            maxFreq = max(maxFreq, freq[s[j]])
            while (j - i + 1 - maxFreq) > k:
                freq[s[i]] -= 1
                i += 1
            ans = max(ans, j - i + 1)
                
        return ans