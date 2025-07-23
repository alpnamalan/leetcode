### JULY 22, 2025 -- P714: BEST TIME TO BUY AND SELL STOCK WITH TRANSACTION FEE ###

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n == 0:
            return 0
        # starting profits IF...
        no_stock = 0
        hold_stock = -prices[0]

        for price in prices:
            # ending up w/o stack at the end of the day
            # we either still did not buy
            # or sold what we had
            new_no_stock = max(no_stock, hold_stock + price - fee)
            # ending up with stack at the end of the day
            # we either kept our stack
            # or we just bought it
            new_hold_stock = max(hold_stock, no_stock - price)

            # update values
            no_stock = new_no_stock
            hold_stock = new_hold_stock
        return no_stock
