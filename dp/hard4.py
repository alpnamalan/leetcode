### AUG 15, 2025 -- P312: BURST BALLOONS ###

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """ Matrix Chain Multiplication–style DP """
        # filter out 0's add 1's to each end
        nums = [1] + [num for num in nums if num > 0] + [1]
        n = len(nums)
        # dp[l][r] = max coins bursting strictly between l & r.
        dp = [[0]*n for _ in range(n)]
        # start at 2 because a gap of 1 means l and r are adjacent
        for gap in range(2, n): # gap between l and r
            for l in range(n - gap):
                r = l + gap
                # If i is last, its neighbors at that moment will be l and r
                for i in range(l+1, r):
                    dp[l][r] = max(
                        dp[l][r],
                        nums[l] * nums[i] * nums[r] + dp[l][i] + dp[i][r]
                    )
        return dp[0][n-1]   
