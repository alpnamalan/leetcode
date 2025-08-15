### AUG 14, 2025 -- P4: MEDIAN OF TWO SORTED ARRAYS ###

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # CORE IDEA:

        # Partition both arrays so that 
        # elements on the left are ≤ elements on the right.
        # Keep the left parts as equal in size as possible.
        if len(nums1) > len(nums2): nums1, nums2 = nums2, nums1
        # nums1 is treated as the smaller one
        m, n = len(nums1), len(nums2)
        total = m+n
        half = total // 2
        # BINARY SEARCH on the smaller array’s partition pt
        lo, hi = 0, m
        while lo <= hi:
            i = (lo+hi)//2 # partition pt in nums1
            j = half-i # partition pt in nums2

            l1  = nums1[i-1] if i > 0 else float('-inf')
            r1 = nums1[i]   if i < m else float('inf')
            l2 = nums2[j-1] if j > 0 else float('-inf')
            r2 = nums2[j]   if j < n else float('inf')
            
            # UNTIL:
            # maxLeftA <= minRightB and maxLeftB <= minRightA
            # Then take the median from the boundary values.
            if l1 <= r2 and l2 <= r1:
                if total % 2:
                    return min(r1, r2)
                return (max(l1, l2) + min(r1, r2)) / 2
            elif l1 > r2: hi = i-1
            else: lo = i+1

        # NAIVE BUT NOT O(log(n+m))
        # from statistics import median
        # return median(sorted(nums1+nums2))
