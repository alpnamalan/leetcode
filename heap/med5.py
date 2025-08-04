### AUG 4, 2025 -- P2542: MAXIMUM SUBSEQUENCE SCORE ###

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        import heapq
        # sort nums2 in descending order so you never have to worry about the minimum
        pairs = sorted(zip(nums2, nums1), reverse=True)
        h, sum1, best = [], 0, 0
        for n2, n1 in pairs:
            heapq.heappush(h, n1) # keep a min-heap of nums1 (of len k)
            sum1 += n1
            if len(h) > k:
                sum1 -= heapq.heappop(h) # kick out the min so the sum is larger
            if len(h) == k:
                best = max(best, sum1 * n2)
                # this makes sense because when len == k we will
                # be at the last n2 of nums2's subsequence that will
                # automatically be the medium given the previous sorting
        return best
