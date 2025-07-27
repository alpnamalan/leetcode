### JULY 27, 2025 -- P435: NON-OVERLAPPING INTERVALS ###

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # GREEDY SOLUTION
        intervals.sort(key=lambda x: x[1])
        toErase = 0
        prev_end = float('-inf')

        for st, end in intervals:
            if st >= prev_end:
                prev_end = end
            else:
                toErase += 1
                
        return toErase
