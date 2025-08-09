### AUG 9, 2025 -- P2537: COUNT THE NUMBER OF GOOD SUBARRAYS ###

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        # PAIR LOGIC == COMBINATORICS LOGIC C(FREQ, 2)
        # ADD ONE NEW, PAIRS += #OLD (1:0 -> 2:1 -> 3:3 -> 4:6)
        # TAKE ONE OUT, PAIRS -= #OLD (4:6 -> 3:3 -> 2:1 -> 1:0)
        freq = defaultdict(int)
        n = len(nums)
        l, pairs, good = 0, 0, 0
        for r in range(n):
            x = nums[r]
            pairs += freq[x] # x will pair with each existing x
            freq[x] += 1
            while pairs >= k:
                good += (n-r) # all extensions should count
                y = nums[l]
                freq[y] -= 1
                pairs -= freq[y] # after decrement, remaining y's are (old-1)
                l += 1
        return good
