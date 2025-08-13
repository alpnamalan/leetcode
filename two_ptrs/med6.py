### AUG 13, 2025 -- P1248: COUNT NUMBER OF NICE SUBARRAYS ###

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """ BEATS 95% IN RUNTIME && 94% IN MEMORY """
        n = len(nums)
        odd = []
        for i, num in enumerate(nums):
            if num & 1:
                odd.append(i)
        o, nice = len(odd), 0
        if o < k: return 0
        for j in range(o-k+1):
            mn, mx = odd[j], odd[j+k-1]
            before = mn+1 if j == 0 else mn-odd[j-1]
            after = n-mx if j == o-k else odd[j+k]-mx
            # print(mn, mx, before, after)
            nice += before*after
        return nice

    # **************************************************************** #

        # STANDARD, EDITORIAL SOLUTION
        # Count subarrays with at most k odd numbers
        # then subtract the count with at most k-1 odd numbers
        # so you're left with exactly k odd nums.

        # def atMost(K):
        #     res = left = count_odd = 0
        #     for right, x in enumerate(nums):
        #         if x & 1:
        #             count_odd += 1
        #         while count_odd > K:
        #             if nums[left] & 1:
        #                 count_odd -= 1
        #             left += 1
        #         res += right - left + 1
        #     return res
        # return atMost(k) - atMost(k - 1)
