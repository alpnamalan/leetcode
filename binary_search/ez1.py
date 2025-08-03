### AUG 3, 2025 -- P278: FIRST BAD VERSION ###

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 0, n
        while (end - start) > 1:
            mid = (start + end) // 2
            if isBadVersion(mid): # if already bad
                end = mid
            else: # not yet
                start = mid
        return end
