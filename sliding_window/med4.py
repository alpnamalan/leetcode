### JULY 27, 2025 -- P209: MINIMUM SIZE SUBARRAY SUM ###

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = len(nums) + 1
        l = 0
        currSum = 0
        for r in range(len(nums)):
            currSum += nums[r]
            while currSum >= target:
                minLength = min(minLength, r-l+1)
                currSum -= nums[l]
                l += 1
        if minLength > len(nums):
            return 0
        else:
            return minLength
