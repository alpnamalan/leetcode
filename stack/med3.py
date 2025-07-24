### JULY 24, 2025 -- P50: POW(X, N) ###

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # NAIVE: EXCEEDS TIME LIMIT
        # curr = 1
        # k = n
        # if n == 0:
        #     return 1
        # if n < 0:
        #     x = 1 / x
        #     k = -k
        # while k > 0:
        #     curr *= x
        #     k -= 1
        # return curr

        # RUNTIME-OPTIMIZED
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        half = self.myPow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x
