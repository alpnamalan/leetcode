### AUG 5, 2025 -- P773: SLIDING PUZZLE ###

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # Does not work with Greedy/DFS (which I initially tried)
        # Need to use BFS and store visited states
        from collections import deque
        init = "".join(str(cell) for row in board for cell in row)
        goal = "123450"
        # dict of "legal moves" across indices in BFS
        adj = {
            0: [1,3],
            1: [0,2,4],
            2: [1,5],
            3: [0,4],
            4: [1,3,5],
            5: [2,4]
        }
        q = deque([(init, 0)]) # store board state and move count
        seen = set([init])
        while q:
            state, moves = q.popleft()
            if state == goal:
                return moves
            zero_idx = state.index('0')
            # for each num you can swap with 0 at its current pos
            for swap in adj[zero_idx]:
                # need to use lists to swap ch in a str
                new_state = list(state)
                new_state[zero_idx], new_state[swap] = new_state[swap], new_state[zero_idx]
                new_str = "".join(new_state)
                if new_str not in seen:
                    seen.add(new_str)
                    q.append((new_str, moves+1))
        # if you never reach the goal after exhausting options
        return -1
