### AUG 18, 2025 -- P1760: MINIMUM LIMIT OF BALLS IN A BAG ###

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        """ HEAP APPROACH DOES NOT WORK BECAUSE
            SPLITTING THE CURRENT MAX INTO HALVES IS NOT
            ALWAYS THE GLOBALLY OPTIMAL SOLUTION !! """
        lo, hi = 1, max(nums)
        while lo < hi:
            mid = (lo+hi) // 2 # penalty cap
            """ If penalty is capped at MID, how many splits to achieve that?
                If num ≤ MID, no splits needed.
                If num > MID, break it into chunks of size ≤ MID."""
            need = sum((num-1) // mid for num in nums)
            if need <= maxOperations: # we can go for even lower penalty
                hi = mid
            else:
                lo = mid+1
        return lo
