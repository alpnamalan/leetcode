### AUG 15, 2025 -- P221: MAXIMAL SQUARE ###

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """ O(m*n) SOLUTION :: BEATS 70% """
        # Recurrence based on left, up and diagonal
        # 1 1 1 | EXAMPLE VIEW: The num on cell denotes
        # 1 2 2 | the len of the square, of which it is
        # 1 2 3 | the bottom right corner.
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*(n+1) for _ in range(m+1)] # padded DP matrix
        best = 0 # side length
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1 + min(
                        dp[i-1][j], dp[i][j-1], dp[i-1][j-1]
                    )
                    best = max(best, dp[i][j])
        return best*best # return its area
