### AUG 5, 2025 -- P532: K-DIFF PAIRS IN AN ARRAY ###

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        from collections import Counter
        cts = Counter(nums)
        total = 0
        # if k == 0, we can only add if there's more than one
        if k == 0:
            for v in cts.values():
                if v > 1: # if duplicate
                    total += 1
            return total
        # else use a set approach for unique pairs
        nums_set = set(cts.keys())
        for num in nums_set:
            if num + k in nums_set:
                total += 1
        return total
