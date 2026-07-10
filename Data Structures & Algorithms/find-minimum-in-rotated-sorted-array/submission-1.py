class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums is None:
            return None
        l = 0
        r = len(nums) - 1
        ans = nums[0]
        while l <= r:
            m = (r+l)//2
            ans = min(ans, nums[m])
            if nums[r] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        return ans
