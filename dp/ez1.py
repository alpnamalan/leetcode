### JULY 3, 2025 -- P70: CLIMBING STAIRS ###

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dp(rest):
            if rest in memo:
                return memo[rest]
            if rest == 1 or rest == 2:
                return rest
            ways = dp(rest - 1) + dp(rest - 2)
            memo[rest] = ways
            return ways
        return dp(n)
