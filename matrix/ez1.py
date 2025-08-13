### AUG 13, 2025 -- P566: RESHAPE THE MATRIX ###

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # BEATS 100% IN RUNTIME && 76% IN MEMORY
        from itertools import chain
        m, n = len(mat), len(mat[0])
        if (m*n != r*c) or m == r and n == c: return mat
        flat = list(chain.from_iterable(mat))
        return [flat[i*c:(i+1)*c] for i in range(r)]
        # out = [[0]*c for _ in range(r)]
        # for i in range(m):
        #     for j in range(n):
        #         idx = i*n + j
        #         row, col = idx // c, idx % c
        #         out[row][col] = mat[i][j]
        # return out
