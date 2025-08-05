### AUG 5, 2025 -- P48: ROTATE IMAGE ###

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # CORE FORMULA: (i,j) --> (j, (n - 1) - i)
        # Would be very easy if I could just allocate a new matrix.
        # INTUITION:
        # To rotate the matrix in place without losing the original values
        # the trick is to rotate 4 elements at a time, layer by layer.
        n = len(matrix)
        for l in range(n // 2): # think of l (layer) as the fixed offset from the edge.
            for i in range(l, n - l - 1): # column range shrinks as you move inwards
                top = matrix[l][i] # top row of the layer, i as col
                # FULL CLOCKWISE ROTATION OF Lth LAYER
                matrix[l][i] = matrix[n-1-i][l] # left -> top
                matrix[n-1-i][l] = matrix[n-1-l][n-1-i] # bottom -> left
                matrix[n-1-l][n-1-i] = matrix[i][n-1-l] # right -> bottom
                matrix[i][n-1-l] = top # top -> right   
