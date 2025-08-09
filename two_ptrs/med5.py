### AUG 9, 2025 -- P189: ROTATE ARRAY ###

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # O(1) EXTRA MEMORY TRICK: CIRCULAR, TWO PTR APPROACH
        from math import gcd
        n = len(nums)
        if n <= 1: return 
        k %= n
        if k == 0: return

        cycles = gcd(n, k)
        for start in range(cycles):
            curr = start
            prev = nums[start]
            while True:
                nxt = (curr + k) % n
                nums[nxt], prev = prev, nums[nxt]  # place, carry
                curr = nxt
                if curr == start:
                    break

        # EASY SOLUTION BEATS 100% IN RUNTIME
        # from collections import deque
        # q = deque(nums)
        # q.rotate(k)
        # nums[:] = list(q)
