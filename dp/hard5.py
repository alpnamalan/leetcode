### AUG 18, 2025 -- P1425: CONSTRAINED SUBSEQUENCE SUM ###

class Solution:
    from collections import deque
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        """ dp[i] = max sum of a valid subsequence ending at i
            && deque of indices with dp values decreasing """
        dp = [0]*n
        q = deque()
        for i, x in enumerate(nums):
            # drop indices out of curr window [i-k, i-1]
            while q and q[0] < i-k:
                q.popleft()
            best = dp[q[0]] if q else 0 # window max or 0 to “start fresh”
            dp[i] = x + max(0, best) # extend or restart
            # maintain decreasing dp in deque
            while q and dp[q[-1]] <= dp[i]:
                q.pop()
            q.append(i)
        return max(dp)
