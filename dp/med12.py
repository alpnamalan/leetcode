### AUG 11, 2025 -- P120: TRIANGLE ###

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # RECURSIVE DP BEATS 85% IN MEMORY (BUT 5% IN RUNTIME)
        # from functools import lru_cache
        # n = len(triangle)
        # if n == 1: return triangle[0][0]
        # @lru_cache()
        # def pathMax(lvl, i):
        #     if lvl == n-2: 
        #         return triangle[lvl][i] + min(triangle[lvl+1][i], triangle[lvl+1][i+1])
        #     else:
        #         return triangle[lvl][i] + min(pathMax(lvl+1, i), pathMax(lvl+1, i+1))
        # return pathMax(0, 0)

        # ITERATIVE DP BEATS 86% IN RUNTIME
        n = len(triangle)
        if n == 1: return triangle[0][0]
        dp = [[0]*(n-i) for i in range(n)]
        # populate bottom level
        dp[0] = triangle[-1]
        # populate rest
        for level in range(1, n):
            for i in range(n-level):
                dp[level][i] = triangle[n-level-1][i] + min(dp[level-1][i], dp[level-1][i+1])
        return dp[n-1][0]

        # SUPER-OPTIMIZED SOLUTION BEATS 86% IN RUNTIME && BEATS 90%+ IN MEMORY
        # LOWKEY A STRETCH, THO
        # dp = triangle[-1][:]      
        # for r in range(len(triangle)-2, -1, -1):
        #     for c in range(r+1):         
        #         dp[c] = triangle[r][c] + min(dp[c], dp[c+1])
        # print(dp)
        # return dp[0]
