#Sudoku Validity
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def valid(r):
            row = set()
            for i in r:
                if i in row:
                    return False
                elif i != ".":
                    row.add(i)
            return True
        

        for r in board:
            if not valid(r):
                return False

        for c in range(0, 9):
            col = set()
            for j in range(9):
                if board[j][c] in col:
                    return False
                elif board[j][c] != ".":
                    col.add(board[j][c])


        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subgrid = []
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        subgrid.extend(board[x][y])
                if not valid(subgrid):
                    return False

        return True
