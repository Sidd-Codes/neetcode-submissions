class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = defaultdict(int)
        freq = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            count[num] = 1 + count[num]
        for num, cnt in count.items():
            freq[cnt].append(num)
        ans = []
        for i in range(len(freq)-1, -1, -1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        return []