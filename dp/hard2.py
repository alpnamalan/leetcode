### AUG 11, 2025 -- P123: BEST TIME TO BUY AND SELL STOCK III ###

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 4-STATE DP:
        # represents “best profit so far given a fixed num of transactions so far,” 
        # and the updates only allow to move forward in that transaction count.
        # two in this case
        buy1 = buy2 = float('-inf')
        sell1 = sell2 = 0
        for p in prices:
            buy1 = max(buy1, -p)
            sell1 = max(sell1, buy1+p)
            buy2 = max(buy2, sell1-p)
            sell2 = max(sell2, buy2+p)
        return sell2
