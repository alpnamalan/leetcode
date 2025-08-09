### AUG 7, 2025 -- P3225: MAXIMUM SCORE FROM GRID OPERATIONS ###

class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        # Honestly this P was so hard that I gave up and copied
        # one of the solutions ://
        # row->range(n); col->range(n+1)
        from itertools import accumulate
        n = len(grid)
        pref = []
        curr = [[0,0] for _ in range(n+1)]
        # process prefix sums
        pref = [list(accumulate(col, initial=0)) for col in zip(*grid)]
        for i in reversed(range(n)): # start from bottom row up
            # prev->prev row, curr->curr row
            prev, curr = curr, [[0,0] for _ in range(n+1)]
            for j, k, opt in product(range(n+1), range(n+1), (0, 1)):
                # j = how many cells painted in current column c
                # k = how many cells painted in previous column c-1
                # opt = c-2 vs. c-1
                if k > j and i != 0 and opt == 1: # c > c-1 > c-2
                    curr[j][1] = max(curr[j][1],
                            pref[i-1][k] - pref[i-1][j] + prev[k][1])
                elif j > k: # c-1 > c
                    curr[j][opt] = max(curr[j][opt], 
                        pref[i][j] - pref[i][k] + prev[k][0])
                else: # c-1 == c
                    curr[j][opt] = max(curr[j][0], prev[k][1])
        return max(*curr[0])
