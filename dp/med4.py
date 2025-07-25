### JULY 22, 2025 -- P1143: LONGEST COMMON SUBSEQUENCE ###

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        dp = [[0] * (l2 + 1) for x in range(l1 + 1)]
        for i in range(l1):
            for j in range(l2):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i+1][j], dp[i][j+1])

        return dp[l1][l2]
