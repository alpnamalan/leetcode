### AUG 1, 2025 -- P128: LONGEST CONSECUTIVE SEQUENCE ###

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        best = 0
        for x in s:
            if x - 1 not in s: # if x - 1 is there, better take that as starting pt
                y = x
                while y in s:
                    y += 1
                best = max(best, y - x)
        return best
