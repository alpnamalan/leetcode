### JULY 24, 2025 -- P2448: MINIMUM COST TO MAKE ARRAY EQUAL ###

class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        # BRUTE-FORCE APPROACH (CORRECT BUT EXCEEDS TIME LIMIT)
        # potential = []
        # for i in range((len(nums))):
        #     curr = 0
        #     for j in range((len(nums))):
        #         curr += (abs(nums[i] - nums[j]) * cost[j])
        #     potential.append(curr)
        # return min(potential)

        # OPTIMIZATION
        # IDEA: total_cost = Σ |nums[i] - x| * cost[i]
        # You choose x such that the 
        # cumulative cost on the left ≈ cumulative cost on the right.
        pairs = sorted(zip(nums, cost))
        total_cost = sum(cost)
        curr = 0
        for num, c in pairs:
            curr += c
            if curr >= (total_cost + 1) // 2:
                med = num
                break
        final = 0
        for num, c in pairs:
            final += abs(num - med) * c
        return final
