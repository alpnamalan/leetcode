### JULY 3, 2025 -- DP: Coin Change Problem ###

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def helper(amt):
            if amt in memo:
                return memo[amt]
            if amt == 0:
                return 0
            if amt < 0:
                return 99999
            result = 1 + min(helper(amt - c) for c in coins)
            memo[amt] = result
            return result
        final = helper(amount)
        if final >= 99999:
            return -1
        else:
            return final
