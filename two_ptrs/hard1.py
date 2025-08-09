### AUG 9, 2025 -- P42: TRAPPING RAIN WATER ###

class Solution:
    def trap(self, height: List[int]) -> int:
        # I first thought of solving it as horizontal slices 
        # but terrible runtime O(n*H)!!
        # OPTIMAL: TWO PTRS O(n)/O(1) --> BEATS 97% IN RUNTIME; 70% IN MEMORY
        l, r = 0, len(height)-1
        lmax, rmax = 0, 0
        water = 0
        """ Water at i is bounded by the shorter wall
            If left_max ≤ right_max, the left cell is “decidable.”
            At every iteration, you know the smaller of left_max and right_max 
            is locked in for its side.
            the shorter side (left_max) is the limiting wall, 
            so water can never rise above it."""
        while l < r:
            lh, rh = height[l], height[r]
            if lh <= rh:
                if lh > lmax: lmax = lh
                water += lmax-lh
                l += 1
            else:
                if rh > rmax: rmax = rh
                water += rmax-rh
                r -= 1
        return water
