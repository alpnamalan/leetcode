### JULY 25, 2025 -- P2352: EQUAL ROW AND COLUMN PAIRS ###

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        from collections import Counter
        # newGrid = []
        # for g in grid:
        #     curr = ""
        #     for x in g:
        #         curr += str(x)
        #         curr += "-"
        #     newGrid.append(curr)
        # gridCtr = Counter(newGrid)
        # n = len(newGrid)
        # equal = 0
        # for i in range(n):
        #     curr_num = ""
        #     for j in range(n):
        #         curr_num += str(grid[j][i])
        #         curr_num += "-"
        #     equal += gridCtr[curr_num]
        # return equal
        rows = [tuple(row) for row in grid]
        cols = [tuple(grid[r][c] for r in range(len(grid))) for c in range(len(grid))]
        rowCts = Counter(rows)
        return sum(rowCts[col] for col in cols)
