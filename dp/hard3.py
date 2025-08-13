### AUG 12, 2025 -- P2809: MINIMUM TIME TO MAKE ARRAY SUM AT MOST X ###

class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        # INTUITION: 
        # earlier resets go to small‐growth items, later resets to big‐growth items.
        # so sort pairs by ascending nums2
        pairs = sorted(zip(nums1, nums2), key=lambda x:x[1])
        n = len(nums1)
        # ************************************************************ #
        # Let dp[i][j] represent the maximum total value that can be reduced
        # if we do j operations on the first i elements
        dp = [[float('-inf')]*(n+1) for _ in range(n+1)]
        dp[0][0] = 0
        # ************************************************************ #
        # TRANSITIONS:
        # Choose the best of:
        # 1) Don't reset this item
        # 2) Reset but make it j-th reset
        for i in range(1, n+1):
            n1, n2 = pairs[i-1]
            dp[i][0] = dp[i-1][0]
            for j in range(1, i+1):
                dp[i][j] = max(
                    dp[i-1][j], # same j, no new operation
                    dp[i-1][j-1] + n1 + j*n2 # gained val with the reset
                )
        # ************************************************************ #
        s1, s2, out = sum(nums1), sum(nums2), -1
        for j in range(n+1):
            # CHECK: 
            # sum if array grew for j seconds w/o resets
            # MINUS max total we can erase via j resets
            if s1 + j*s2 - dp[n][j] <= x:
                out = j
                break # break early so we get the earliest j
        return out
