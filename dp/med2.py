### JULY 3, 2025 -- P198: HOUSE ROBBER ###

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]
            sum = nums[i]
            if i + 3 < len(nums):
                sum = sum + max(dp(i+2), dp(i+3))
            elif i + 2 < len(nums):
                sum = sum + dp(i+2)
            memo[i] = sum
            return sum
        total = max(dp(0), dp(1))
        return total
