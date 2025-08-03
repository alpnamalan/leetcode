### AUG 4, 2025 -- P1011: CAPACITY TO SHIP PACKAGES WITHIN D DAYS ###

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # BEATS ~90% IN RUNTIME AND USES O(1) EXTRA SPACE
        def possible(cap):
            left, time = cap, 1
            for w in weights:
                if w <= left:
                    left -= w
                else:
                    time += 1
                    left = cap - w
            return time <= days
        lo, hi = max(weights), sum(weights)
        while lo < hi:
            mid = (lo + hi) // 2
            if possible(mid): # if cap is enough, maybe it's higher than min
                hi = mid
            else:
                lo = mid + 1
        return lo
