### AUG 13, 2025 -- P528: RANDOM PICK WITH WEIGHT ###

class Solution:
    import random
    """ INITIAL APPROACH EXCEEDS MEM LIMIT
        USE PREFIX SUM + BISEARCH INSTEAD!! 
        BEATS 80% IN RUNTIME """
    # from itertools import repeat
    # def __init__(self, w: List[int]):
    #     self.nums = []
    #     for i, wt in enumerate(w):
    #         self.nums.extend(repeat(i, wt))
    # def pickIndex(self) -> int:
    #     return random.choice(self.nums)
    from bisect import bisect_left
    def __init__(self, w: List[int]):
        self.pref, s = [], 0
        for wt in w:
            s += wt
            self.pref.append(s)
        self.total = s

    def pickIndex(self) -> int:
        r = random.randint(1, self.total)
        return bisect_left(self.pref, r)
    # Why it works: each index i owns the interval 
    # (pref[i-1], pref[i]] of length w[i]
    # sampling a uniform x in [1, total] hits 
    # interval i with probability w[i]/total.
