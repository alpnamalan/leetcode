### JULY 22, 2025 -- P1493: LONGEST SUBARRAY OF 1'S AFTER DELETING ONE ELEMENT ###

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        zeros = 0
        left = 0
        # KEY: sliding window with at most one zero
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            if (right - left + 1) > res:
                res = right - left + 1
                
        return res - 1
