### JULY 27, 2025 -- P746: MIN COST CLIMBING STAIRS ###

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        from functools import lru_cache
        idx = len(cost) - 1
        @lru_cache()
        def dp(idx):
            if idx < 2:
                return cost[idx]
            else:
                return cost[idx] + min(dp(idx - 1), dp(idx - 2))
        return min(dp(idx), dp(idx - 1))
