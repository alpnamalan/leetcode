### AUG 6, 2025 -- P2812: FIND THE SAFEST PATH IN A GRID ###

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        from collections import deque
        ### PART 1: SAFENESS GRID ###
        # grid with safeness factors via multi-source BFS
        n = len(grid)
        safeness = [[-1]*n for x in range(n)]
        q = deque()
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    safeness[row][col] = 0 
                    q.append((row, col))
        # execute multi-source BFS
        # save highest factor for the binary-search in Part 2
        # low, high = 0, 0
        dirs = ((1,0), (-1,0), (0,1), (0,-1))
        while q:
            r, c = q.popleft()
            for dx, dy in dirs:
                nr, nc = r+dx, c+dy
                # if within the grid and hasn't been populated
                if 0 <= nr < n and 0 <= nc < n and safeness[nr][nc] == -1:
                    safeness[nr][nc] = safeness[r][c] + 1
                    # high = max(high, safeness[nr][nc])
                    q.append((nr, nc))

        ### OPTIMIZED PART 2 WITH DIJKSTRA'S ALGO ###
        # BEATS ~70% IN RUNTIME AND 72% IN MEMORY!
        from heapq import heappush, heappop
        maxheap = [(-safeness[0][0], 0, 0)] # negated vals bc we want a max heap
        visited = [[False]*n for x in range(n)]
        while maxheap:
            safe, r, c = heappop(maxheap)
            safe = -safe # revert to original
            if (r, c) == (n-1, n-1): # reached end
                return safe
            if visited[r][c]: continue
            else: visited[r][c] = True
            for dx, dy in dirs:
                nr, nc = r+dx, c+dy
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    # the new safeness is the min of path so far and new cell
                    next_safeness = min(safe, safeness[nr][nc])
                    heappush(maxheap, (-next_safeness, nr, nc))
        return 0 
        ### PART 2: LOOK FOR THE OPTIMAL PATH VIA BFS (BEATS 23% IN RUNTIME) ###
        # def possible(lim) -> bool: # graph traversal
        #     if safeness[0][0] < lim: return False
        #     q = deque([(0, 0)])
        #     seen = {(0,0)}
        #     target = (n-1, n-1)
        #     if target == (0,0): return True
        #     while q:
        #         r, c = q.popleft()
        #         if (r, c) == target: return True
        #         for dx, dy in dirs:
        #             nr, nc = r+dx, c+dy
        #             if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in seen and safeness[nr][nc] >= lim:
        #                 seen.add((nr, nc))
        #                 q.append((nr, nc)) # only add if it's above the min threshold
        #     return False
        # high += 1 # for exclusive upper bound
        # while low+1 < high: # binary search
        #     lim = (high + low) // 2
        #     if possible(lim): low = lim # try higher
        #     else: high = lim
        # return low
