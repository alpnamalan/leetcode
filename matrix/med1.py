### AUG 5, 2025 -- P54: SPIRAL MATRIX ###

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        # these should correspond to r, d, l, u given
        # how 2D arrays work
        di = 0
        dr = dirs[di]
        nums = []
        visited = set()
        pos = (0, 0)
        visited.add(pos)
        nums.append(matrix[pos[0]][pos[1]])
        while len(visited) < m*n:
            new_pos = (pos[0] + dr[0], pos[1] + dr[1])
            while new_pos not in visited and 0 <= new_pos[0] < m and 0 <= new_pos[1] < n:
                pos = new_pos
                visited.add(pos)
                nums.append(matrix[pos[0]][pos[1]])
                new_pos = (pos[0] + dr[0], pos[1] + dr[1])
            di += 1
            dr = dirs[di % 4]
        return nums
