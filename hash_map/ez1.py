### JULY 6, 2025 -- P1207: UNIQUE NUMBER OF OCCURRENCES ###

from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ## MEMORY-EFFICIENT BUT NOT RUNTIME-EFFICIENT
        # count = Counter(arr)
        # cc = Counter(list(count.values()))
        # for c in list(cc.values()):
        #     if c != 1:
        #         return False
        # return True

        counts = Counter(arr).values()
        uniq = set(counts)
        return len(counts) == len(uniq)
