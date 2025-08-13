### AUG 13, 2025 -- P525: CONTIGUOUS ARRAY ###

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # PREFIX SUM + HASH MAP :: BEATS 99% IN RUNTIME
        sm = 0
        seenSum = {0:0} # (sum: earliest idx)
        best = 0
        for i, num in enumerate(nums, 1):
            sm += 1 if num == 1 else -1
            if sm in seenSum:
                ln = i-seenSum[sm]
                if ln > best: best = ln
            else: seenSum[sm] = i
        return best
