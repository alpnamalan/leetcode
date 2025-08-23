### AUG 17, 2025 -- P57: INSERT INTERVAL ###

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        from bisect import bisect_left
        i = bisect_left(intervals, [newInterval[0], float('-inf')])
        ns, ne = newInterval
        left, right = i-1, i
        while left >= 0:
            s, e = intervals[left]
            if ns <= e:
                ns, ne = s, max(e, ne)
                left -= 1
            else: break
        while right < len(intervals):
            s, e = intervals[right]
            if ne >= s:
                ns, ne = ns, max(e, ne)
                right += 1
            else: break
        return intervals[:left+1] + [[ns, ne]] + intervals[right:]
