### AUG 16, 2025 -- P918: MAXIMUM SUM CIRCULAR SUBARRAY ###

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """ KADANE'S ALGORITHM WITH A TWIST 
            The best circular subarray is either:  
            non-wrapping max subarray, or
            wraps around, which equals total - middle """
        # Standard Kadane's
        currMax = bestMax = nums[0]
        # For the wrap-around case
        total = currMin = bestMin = nums[0]
        for x in nums[1:]:
            # Standard Kadane's
            currMax = max(currMax+x, x)
            bestMax = max(bestMax, currMax)
            # For potential wrap-around
            total += x
            currMin = min(x, currMin+x)
            bestMin = min(currMin, bestMin)
        #  If all negatives, wrapping would be empty -> invalid
        if bestMax < 0: return bestMax
        return max(bestMax, total - bestMin)
