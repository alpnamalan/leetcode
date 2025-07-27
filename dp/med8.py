### JULY 27, 2025 -- P790: DOMINO AND TROMINO TILING ###

class Solution:
    def numTilings(self, n: int) -> int:
        dp, half = [0] * (n+1), [0] * (n+1)
        mod = 10**9 + 7
        # Base cases
        for i in range(n + 1):
            if i < 2:
                dp[i] = 1
            else:
                dp[i] = (dp[i-1] + dp[i-2] + 2 * half[i-1]) % mod
                half[i] = (half[i-1] + dp[i-2]) % mod
        return dp[n]
