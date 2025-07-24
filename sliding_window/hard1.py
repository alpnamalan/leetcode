### JULY 24, 2025 -- P220: CONTAINS NEARBY ALMOST DUPLICATE ###

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        from sortedcontainers import SortedList
        sl = SortedList()
        for i in range(len(nums)):
            idx = sl.bisect_left(nums[i] - valueDiff)
            if idx < len(sl) and abs(sl[idx] - nums[i]) <= valueDiff:
                return True
            sl.add(nums[i])
            if i >= indexDiff: # removes one at a time, but it's OK because we increment by one anyway
                sl.remove(nums[i - indexDiff])
        return False
