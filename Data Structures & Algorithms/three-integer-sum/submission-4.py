class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and nums[i-1] == a:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = a + nums[l] + nums[r]
                if total == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return ans

