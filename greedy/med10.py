### AUG 13, 2025 -- P56: MERGE INTERVALS ###

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        merged = [intervals[0]]
        for s, e in intervals[1:]:
            if s <= merged[-1][1]: # starts before or when prev ends
                merged[-1][1] = max(merged[-1][1], e)
            else:
                merged.append([s,e])
        return merged
