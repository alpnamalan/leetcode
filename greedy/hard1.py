### AUG 2, 2025 -- P135: CANDY ###

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        # LEFT -> RIGHT PASS
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        # RIGHT -> LEFT PASS
        for i in range(n - 2, -1, -1):
            # only fix if it's decreasing
            if ratings[i] > ratings[i+1] and candies[i] <= candies[i + 1]:
                candies[i] = candies[i+1] + 1
            
        return sum(candies)
