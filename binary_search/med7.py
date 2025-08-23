### AUG 17, 2025 -- P852: PEAK INDEX IN A MOUNTAIN ARRAY ###

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # BINARY SEARCH:
        # Increasing -> before the peak
        # Decreasing -> after the peak
        lo, hi = 0, len(arr)-1
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] < arr[mid+1]: # rising slope, mid+1 could be peak
                lo = mid+1
            else: # falling slope, mid could be peak
                hi = mid
        return lo
