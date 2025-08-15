### AUG 14, 2025 -- P74: SEARCH A 2D MATRIX ###

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """ O(log(m * n)) SOLUTION VIA BINARY SEARCH """
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m*n-1
        while lo <= hi:
            mid = (lo + hi) // 2
            i, j = divmod(mid, n)
            if target == matrix[i][j]:
                return True
            elif target > matrix[i][j]:
                lo = mid+1
            else:
                hi = mid-1
        return False
