class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            numbers = [int(cell) for cell in row if cell.isdigit()]
            if len(numbers) != len(set(numbers)) or any(n > 9 or n < 1 for n in numbers):
               return False
        for column in zip(*board):
            numbers = [int(cell) for cell in column if cell.isdigit()]
            if len(numbers) != len(set(numbers)) or any(n > 9 or n < 1 for n in numbers):
                return False
        for box_row in range(0, 9 , 3):
            for box_column in range(0, 9, 3):
                box = [board[i][j] for i in range(box_row, box_row + 3) for j in range(box_column, box_column + 3)]
                box = [int(cell) for cell in box if cell.isdigit()]
                if len(box) != len(set(box)) or any(n > 9 or n < 1 for n in box):
                    return False
        return True

    