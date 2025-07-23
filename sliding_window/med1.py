### JULY 6, 2025 -- P1004: MAX CONSECUTIVE ONES III ###

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_ones = 0
        left = 0
        flips = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                flips += 1  
            while flips > k:
                if nums[left] == 0:
                    flips -= 1
                left += 1
            max_ones = max(max_ones, right - left + 1)

        return max_ones
