### JULY 27, 2025 -- P452: MINIMUM NUMBER OF ARROWS TO BURST BALLOONS ###

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # GREEDY STRATEGY
        # shoot at the earliest end of the current overlapping group
        points.sort(key=lambda x:x[1])
        range_end = float('-inf')
        arrows = 0
        for st, end in points:
            if st > range_end: 
                arrows += 1
                range_end = end           
            # otherwise, there is some overlap, can burst with the same arrow
        return arrows
