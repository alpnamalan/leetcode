### AUG 5, 2025 -- P1020: NUMBER OF ENCLAVES ###

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        from collections import deque
        m, n = len(grid), len(grid[0])
        dirs = ((1,0),(0,1),(-1,0),(0,-1))
        # INTUITION: FLOOD-FILL FROM THE BORDER
        def walk(sr, sc):
            q = deque([(sr, sc)])
            grid[sr][sc] = 0 # mark walkable land as 0
            while q:
                r, c = q.popleft()
                for d1, d2 in dirs: # check each adjacent nbor
                    nr, nc = r+d1, c+d2
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 0 # neigbor is also walkable
                        q.append((nr, nc))
        # only loop through border cells
        for r in range(m):
            # top/bottom rows
            if r == 0 or r == m-1:
                for c in range(n):
                    if grid[r][c] == 1: walk(r, c)
            else: # just left and right borders
                for c in [0, n-1]:
                    if grid[r][c] == 1: walk(r, c)
        # Count pieces of land you can't reach from the border
        ct = 0
        for r in range(1,m-1):
            for c in range(1,n-1):
                if grid[r][c] == 1: ct += 1
        return ct
