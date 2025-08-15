### AUG 15, 2025 -- P63: UNIQUE PATHS II ###

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i > 0: dp[i][j] += dp[i-1][j]
                if j > 0: dp[i][j] += dp[i][j-1]
                # The only catch is when you encounter an obstacle
                # set its value in DP to 0
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
        return dp[m-1][n-1]
