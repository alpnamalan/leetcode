### JULY 27, 2025 -- P560: SUBARRAY SUM EQUALS K ###

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Sliding window does NOT work for this P
        # CORE LOGIC:
        # If prefix_sum[i] - prefix_sum[j] == k, then the subarray nums[j+1...i] has sum k.
        from collections import defaultdict
        curr_sum = 0
        ans = 0
        seen = defaultdict(int)
        seen[0] = 1

        for num in nums:
            curr_sum += num
            ans += seen[curr_sum - k]
            seen[curr_sum] += 1
        
        return ans
