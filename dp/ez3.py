### AUG 9, 2025 -- P121: BEST TIME TO BUY AND SELL STOCK ###

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn, ans = 10**18, 0
        for p in prices:
            if p < mn: mn = p # min will be 1
            if p-mn > ans: ans = p-mn # ans will be 6-1
        return ans
