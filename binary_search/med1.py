### JULY 24, 2025 -- P875: KOKO EATING BANANAS ###

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        low, high = 1, max(piles)
        # BINARY SEARCH
        while low < high:
            # DETERMINE CURRENT SPEED
            middle = (low + high) // 2
            time = 0
            # REQUIRED TOTAL TIME WITH CURRENT SPEED
            for p in piles:
                time += math.ceil(p / middle)
            # IF ENOUGH, THE OPTIMAL SPEED IS LOWER THAN MIDDLE
            if time <= h:
                high = middle
            # IF NOT, YOU NEED A HIGHER SPEED
            else:
                low = middle + 1
        return low
