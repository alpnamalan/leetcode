### JULY 24, 2025 -- P480: SLIDING WINDOW MEDIAN ###

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        from sortedcontainers import SortedList
        sl = SortedList(nums[:k])
        meds = []
        # Set up left-most window
        if k % 2 == 1:
            med = sl[(k // 2)]
        elif k == 0:
            return meds
        else:
            med1 = sl[(k // 2) - 1]
            med2 = sl[(k // 2)]
            med = (med1 + med2) / 2
        meds.append(float(med))
        # Slide the window to the right
        for r in range(k, len(nums)):
            sl.add(nums[r])
            sl.remove(nums[r - k])
            if k % 2 == 1:
                med = sl[(k // 2)]
            else:
                med1 = sl[(k // 2) - 1]
                med2 = sl[(k // 2)]
                med = (med1 + med2) / 2
            meds.append(float(med))
        return meds
