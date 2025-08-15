### AUG 14, 2025 -- P15: 3SUM ###

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """ SORT + TWO PTRS + SKIP DUPS
        Sorting makes the “move left/right” logic work 
        and lets you skip duplicates in O(1). """
        nums.sort()
        n = len(nums)
        tri = []
        for i in range(n-2):
            if i and nums[i] == nums[i-1]: 
                continue # same 1st el could cause dup triplets
            l, r = i+1, n-1
            target = -nums[i]
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    tri.append([nums[i], nums[l], nums[r]])
                    l += 1; r -= 1
                    # skip if duplicate (for L & R)
                    while l < r and nums[l] == nums[l-1]: l += 1
                    while l < r and nums[r] == nums[r+1]: r -= 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        return tri
