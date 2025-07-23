### JULY 22, 2025 -- P62: UNIQUE PATHS ###

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        import math
        total = (m - 1) + (n - 1)
        ways = math.comb(total, n - 1)
        return ways
