### AUG 16, 2025 -- P36: VALID SUDOKU ###

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """ SINGLE PASS SOLUTION
            BEATS 100% IN RUNTIME && 92% IN MEMORY"""
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.': continue
                b = (i//3) * 3 + (j//3) # Determine which box it falls under
                if val in rows[i] or val in cols[j] or val in boxes[b]:
                    return False
                rows[i].add(val); cols[j].add(val); boxes[b].add(val)
        return True

        """ SEPARATE PASSES :: WORKING YET SLOW """
        # # 1. Validate rows
        # for i in range(9):
        #     row = set()
        #     for j in range(9):
        #         num = board[i][j]
        #         if num.isdigit() and num not in row:
        #             row.add(num)
        #         elif num in row:
        #             return False
        # # 2. Validate cols
        # for j in range(9):
        #     col = set()
        #     for i in range(9):
        #         num = board[i][j]
        #         if num.isdigit() and num not in col:
        #             col.add(num)
        #         elif num in col:
        #             return False
        # # 3. Validate boxes
        # # b0 -> 0,0; b1 -> 0,3;.. b3 -> 3,0
        # for b in range(9):
        #     # coordinates of the bottom left corner
        #     r, c = divmod(b*3, 9)
        #     r *= 3
        #     box = set()
        #     for i in range(r, r+3):
        #         for j in range(c, c+3):
        #             num = board[i][j]
        #             if num.isdigit() and num not in box:
        #                 box.add(num)
        #             elif num in box:
        #                 return False
        # return True
