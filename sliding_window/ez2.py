### JULY 14, 2025 -- P3105: LONGEST STRICTLY INCREASING OR STRICTLY DECREASING SUBARRAY ###

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        l1 = 0
        max_inc = 0
        for r1 in range(len(nums)):
            while l1 < r1 and nums[r1] <= nums[r1 - 1]:
                l1 += 1
            max_inc = max(r1 - l1 + 1, max_inc)

        l2 = 0
        max_dec = 0
        for r2 in range(len(nums)):             
            while l2 < r2 and nums[r2] >= nums[r2 - 1]:
                l2 += 1
            max_dec = max(r2 - l2 + 1, max_dec)
        
        return max(max_inc, max_dec)
