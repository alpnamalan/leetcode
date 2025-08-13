### AUG 10, 2025 -- P152: MAXIMUM PRODUCT SUBARRAY ###

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """ Multiplication by a neg flips large ↔ small.
        A very neg pdt can become the largest if multiplied by another neg.
        Need to track both the max and min pdts up to that point."""
        maxp = minp = best = nums[0]
        for num in nums[1:]:
            if num < 0: maxp, minp = minp, maxp
            maxp = max(maxp*num, num)
            minp = min(minp*num, num)
            best = max(best, maxp)
        return best
