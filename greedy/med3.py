### AUG 2, 2025 -- P55: JUMP GAME ###

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Backward approach
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        if goal == 0:
            return True
        else:
            return False
