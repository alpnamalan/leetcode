### AUG 4, 2025 -- P994: ROTTING ORANGES ###

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        m, n = len(grid), len(grid[0])
        fresh = 0
        q = deque()
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1: fresh += 1
                elif grid[row][col] == 2: q.append((row, col))
        mins = 0
        dirs = ((1,0), (-1,0), (0,1), (0,-1))
        while q and fresh > 0:
            for src in range(len(q)): # one minute worth of spread
                r, c = q.popleft()
                for dir1, dir2 in dirs: # check neighbors in 4 directions
                    nr, nc = dir1 + r, dir2 + c
                    # if neighbor is inside the grid and is fresh orange
                    if (0 <= nr < m and 0 <= nc < n) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2 
                        fresh -= 1
                        q.append((nr, nc))
            mins += 1
        return -1 if fresh > 0 else mins
