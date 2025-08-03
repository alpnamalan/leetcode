### AUG 4, 2025 -- P373: FIND K PAIRS WITH SMALLEST SUMS ###

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # INTUITION:
        # Picture the sums as an n1 × n2 grid 
        # where row i is [nums1[i]+nums2[0], nums1[i]+nums2[1], …]
        # seed the heap with the first cell of each of the first min(k, n1) rows
        # pop the smallest, and only push that row’s next cell
        n1, n2 = len(nums1), len(nums2)
        import heapq
        h = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, n1))]
        heapq.heapify(h)
        out = []
        while h and len(out) < k:
            val, i, j = heapq.heappop(h)
            out.append([nums1[i], nums2[j]])
            if j + 1 < n2:
                heapq.heappush(h, (nums1[i] + nums2[j+1], i, j+1))
        return out
