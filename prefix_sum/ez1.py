### JULY 6, 2025 -- P1732: FIND THE HIGHEST ALTITUDE ###

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = 0
        high = curr
        for g in gain:
            curr += g
            if curr > high: ## calling max() is not runtime efficient
                high = curr
        return high
