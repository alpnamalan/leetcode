### JULY 6, 2025 -- P1679: MAX NUMBER OF K-SUM PAIRS ###

from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ops = 0
        counts = Counter(nums)

        for num in list(counts.keys()):
            comp = k - num
            if comp not in counts:
                continue
            if num == comp:
                pairs = counts[num] // 2
            else:
                pairs = min(counts[num], counts[comp])
            ops += pairs
            counts[num] -= pairs
            counts[comp] -= pairs

        return ops

        # def helper(num, k):
        #     if num is None:
        #         return 0
        #     for i in range(0, len(num)):
        #         curr = num[i]
        #         comp = k - curr
        #         if comp in num[:i] or comp in num[i+1:]:
        #             num.remove(comp)
        #             num.remove(curr)
        #             return (1 + helper(num, k))
        #     return 0
        # ops = helper(nums, k)
        # return ops
