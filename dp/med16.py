### AUG 17, 2025 -- P931: MINIMUM FALLING PATH SUM ###

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        """ BEATS 90%+ IN RUNTIME """
        n = len(matrix)
        dp = [[0]*n for _ in range(n)]
        dp[-1] = matrix[-1] # bottom row is the same
        for r in range(n-2, -1, -1):
            for c in range(n):
                if c == 0: # left edge
                    dp[r][c] = matrix[r][c] + min(
                        dp[r+1][c], dp[r+1][c+1]
                    )
                elif c == n-1: # right edge
                    dp[r][c] = matrix[r][c] + min(
                        dp[r+1][c], dp[r+1][c-1]
                    )
                else: # middle
                    dp[r][c] = matrix[r][c] + min(
                        dp[r+1][c-1], dp[r+1][c], dp[r+1][c+1]
                    )
        return min(dp[0])
