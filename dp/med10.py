### AUG 9, 2025 -- P122: BEST TIME TO BUY AND SELL STOCK II ###

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold, no = -10**4, 0 # hold vs not hold stock
        # set hold to -INF, otherwise you'd never buy bc max(0, 0-p) always 0
        for p in prices:
            if no-p > hold: hold = no-p # should i keep holding or buy new?
            if hold+p > no: no = hold+p # should i do nothing or sell what i have?
        return no
