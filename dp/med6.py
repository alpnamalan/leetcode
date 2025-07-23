### JULY 22, 2025 -- P72: EDIT DISTANCE ###

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Set up matrix
        l1, l2 = len(word1), len(word2)
        dp = [[0] * (l2 + 1) for x in range(l1 + 1)]

        # Set up base cases
        for i in range(l1 + 1):
            dp[i][0] = i
        for j in range(l2 + 1):
            dp[0][j] = j

        # Main loop
        for i in range(l1):
            for j in range(l2):
                # Other scenarios
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    # if not the same, take the most convenient of the
                    # three permitted operations
                    dp[i+1][j+1] = min(
                        # delete
                        dp[i][j+1] + 1,
                        # insert
                        dp[i+1][j] + 1,
                        # replace
                        dp[i][j] + 1
                    )
        return dp[l1][l2]
