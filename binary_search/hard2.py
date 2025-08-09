### AUG 8, 2025 -- P719: FIND K-TH SMALLEST PAIR DISTANCE ###

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        # TWO PTRS
        def dists_under(x):
            i, ct = 0, 0
            for j in range(n):
                while nums[j]-nums[i] > x:
                    i += 1
                ct += j-i
            return ct
        # BINARY SEARCH
        lo, hi = 0, nums[-1]-nums[0]
        while lo < hi:
            mid = (lo + hi) // 2
            # enough pairs <= mid ??
            if dists_under(mid) >= k:
                hi = mid
            else:
                lo = mid+1
        return lo
        # NAIVE HEAP APPROACH BUT TLEs
        # import heapq
        # h = []
        # for i, n1 in enumerate(nums):
        #     for n2 in nums[i+1:]:
        #         dist = abs(n2-n1)
        #         if len(h) < k:
        #             heapq.heappush(h, -dist)
        #         elif dist < -(h[0]): # h[0] is the max of K min distances
        #             heapq.heapreplace(h, -dist)
        # return -heapq.heappop(h)
