### JULY 24, 2025 -- P219: CONTAINS NEARBY DUPLICATE ###

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # from collections import Counter
        # n = k + 1
        # if len(nums) < (k + 1):
        #     n = len(nums)
        # cts = Counter(nums[:n])
        # for r in range(n):
        #     if cts[nums[r]] > 1:
        #         return True
        # for r in range(k+1, len(nums)):
        #     cts[nums[r]] += 1
        #     cts[nums[r-k-1]] -= 1
        #     if cts[nums[r]] > 1:
        #         return True
        # return False

        # BETTER SOLUTION
        seen = set()
        for i, num in enumerate(nums):
            if num in seen:
                return True
            seen.add(num)
            if len(seen) > k:
                seen.remove(nums[i-k])
        return False
