### JULY 6, 2025 -- P11: CONTAINER WITH MOST WATER ###

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l, r = 0, len(height) - 1
        while l < r:
            h = min(height[r], height[l])
            width = r - l
            max_area = max(max_area, h * width)

            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return max_area
