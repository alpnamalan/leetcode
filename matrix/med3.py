### AUG 5, 2025 -- P498: DIAGONAL TRAVERSE ###

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        # CORE INTUITION:
        # i + j == d where d is the 'diagonal number'
        # bottom -> top when d is even and vice versa when it's odd
        # max d is (m-1)+(n-1) i.e., the indices of the last element
        nums = []
        for d in range(m+n-1):
            # first do all from top to bottom and reverse if needed (when d is even)
            line = []
            """CONSTRAINTS: 0 <= i < m; 0 <= j < n
            You want to iterate over all valid row indices i such that:
            * i is within bounds: 0 ≤ i < m
            * and j = d - i is also within bounds: 0 ≤ j < n"""
            for i in range(max(0, d-n+1), min(m, d+1)):
                j = d - i
                line.append(mat[i][j])
            if d % 2 == 0:
                nums.extend(reversed(line))
            else:
                nums.extend(line)
        return nums
