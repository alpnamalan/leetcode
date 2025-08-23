### AUG 21, 2025 -- P212: WORD SEARCH II ###

class TNode:
    """ Classes have __dict__ behind them but it's memory-heavy """
    __slots__ = ("children", "word")
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        # 1. Populate Trie structure with target words
        root = TNode() 
        for w in words:
            node = root
            for ch in w:
                if ch not in node.children:
                    node.children[ch] = TNode()
                node = node.children[ch]
            node.word = w
        # 2. Check paths on the board via DFS
        out = []
        def dfs(r, c, node):
            ch = board[r][c]
            # abort if dead end
            if ch not in node.children: 
                return
            node = node.children[ch]
            if node.word:
                out.append(node.word)
                node.word = None # prevents duplicates
            board[r][c]= '.' # mark as visited to prevent cycles
            # explore neighbors: r-1, r+1, c-1, c+1
            if r > 0 and board[r-1][c] != '.':
                dfs(r-1, c, node)
            if r+1 < m and board[r+1][c] != '.':
                dfs(r+1, c, node)
            if c > 0 and board[r][c-1] != '.':
                dfs(r, c-1, node)
            if c+1 < n and board[r][c+1] != '.':
                dfs(r, c+1, node)
            board[r][c] = ch # restore for future

        # 3. Call DFS to execute solution
        for i in range(m):
            for j in range(n):
                # call DFS only when the curr cell has a
                # valid starting letter
                if board[i][j] in root.children:
                    dfs(i, j, root)
        return out
