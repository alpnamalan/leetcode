### AUG 18, 2025 -- P2187: MINIMUM TIME TO COMPLETE TRIPS ###

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        """ BINARY SEARCH ON ANSWER (BSOA) PROBLEM """
        fast = min(time)
        lo, hi = fast, totalTrips * fast
        while lo < hi:
            mid = (lo + hi) // 2 # time cap
            trips = sum(mid // t for t in time) # completed trips within time cap
            if trips >= totalTrips:
                hi = mid
            else:
                lo = mid+1
        return lo 
