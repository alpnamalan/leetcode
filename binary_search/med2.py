### AUG 1, 2025 -- P2300: SUCCESSFUL PAIRS OF SPELLS AND POTIONS ###

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        from sortedcontainers import SortedList
        import math
        pot = SortedList(potions)
        m = len(pot)
        ans = []
        for s in spells:
            at_least = math.ceil(success / s)
            idx = pot.bisect_left(at_least)
            ans.append(m - idx)
        return ans
