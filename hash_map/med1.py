### JULY 22, 2025 -- P1010: PAIRS OF SONGS WITH TOTAL DURATIONS DIVISIBLE BY 60 ###

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        num = 0
        size60 = 60 * [0]
        for t in time:
            idx = t % 60
            num += size60[(60 - idx) % 60]
            size60[idx] += 1
        return num
