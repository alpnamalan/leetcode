### AUG 2, 2025 -- P200: NUMBER OF ISLANDS ###

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        islands = 0
        m, n = len(grid), len(grid[0])

        # mark every connected "1" as visited via BFS
        def bfs(sr, sc): # sr: start row; sc: start col
            q = deque([(sr, sc)])
            grid[sr][sc] = "visited"
            while q:
                r, c = q.popleft() # next cell to process (FIFO)
                for dir1, dir2 in ((1,0), (-1,0), (0,1), (0,-1)): # check neighbors in 4 directions
                    nr, nc = dir1 + r, dir2 + c
                    # if neighbor is inside the grid and is land
                    if (0 <= nr < m and 0 <= nc < n) and grid[nr][nc] == '1':
                        grid[nr][nc] = "visited" # mark it as visited
                        q.append((nr, nc))

        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    islands += 1
                    # FLOOD-FILL ENTIRE ISLAND AS VISITED
                    bfs(row, col)

        return islands
