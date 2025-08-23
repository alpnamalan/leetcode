### AUG 18, 2025 -- P862: SHORTEST SUBARRAY WITH SUM AT LEAST K ###

class Solution:
    from collections import deque
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        """ NEGATIVES BREAK SLIDING WINDOW APPROACH !! """
        # 1. PREFIX SUMS
        n = len(nums)
        pref = [0]*(n+1)
        for i, x in enumerate(nums):
            pref[i+1] = pref[i] + x
        # 2. QUEUE OF INDICES
        out = n+1
        q = deque()
        for i, p in enumerate(pref):
            # At each r, find the earliest l where pref[r] - pref[l] ≥ k
            while q and p - pref[q[0]] >= k:
                # q[0] is a valid starting idx
                out = min(out, (i - q.popleft()))
            # Deque holds only “best” starts
            # New smaller prefix --> any larger ones behind it are useless.
            while q and pref[q[-1]] >= p:
                q.pop()
            q.append(i)
        return out if out <= n else -1
