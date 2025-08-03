### AUG 4, 2025 -- P215: KTH LARGEST ELEMENT IN AN ARRAY ### 

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # KEEP A MIN-HEAP OF SIZE K
        import heapq
        h = nums[:k]
        heapq.heapify(h)
        for x in nums[k:]:
            if x > h[0]: # if x is larger than the root
                heapq.heapreplace(h, x)
        return h[0]
