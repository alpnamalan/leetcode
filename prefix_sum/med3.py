### AUG 18, 2025 -- P974: SUBARRAY SUMS DIVISIBLE BY K ###

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        freq = [0]*k # frequency of each remainder
        freq[0] = 1 # include empty prefix
        out = rem = 0 
        for x in nums:
            rem = (rem + x) % k # curr remainder
            out += freq[rem] # all earlier prefixes with same remainder
            freq[rem] += 1
        return out   
