### AUG 22, 2025 -- P79: WORD SEARCH ###

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """ DFS + BACKTRACKING """
        m, n = len(board), len(board[0])
        def dfs(r, c, pos): 
            # previously used a need list but in-place 
            # modifications are a mess!!
            if pos == len(word): return True
            if not (0 <= r < m and 0 <= c < n): return False
            if board[r][c] != word[pos]: return False
            # BACKTRACKING SKELETON
            ch = board[r][c]
            board[r][c] = '#'
            for (nr, nc) in [(r-1,c), (r+1,c), (r, c-1), (r, c+1)]:
                if dfs(nr, nc, pos+1): return True
                # propagate results ONLY if they're true
            board[r][c] = ch
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0): return True
        return False
