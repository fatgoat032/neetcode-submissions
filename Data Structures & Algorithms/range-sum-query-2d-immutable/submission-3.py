class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.arr_ = matrix
        rows = len(matrix) + 1
        columns = len(matrix[0]) + 1
        self.arr_ = [[0] * columns for i in range(rows)]
        for r in range(rows):
            for c in range(columns):
                self.arr_[r][c] = matrix[r - 1][c - 1] + self.arr_[r - 1][c] + self.arr_[r][c - 1] - self.arr_[r - 1][c - 1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.arr_[row2 + 1][col2 + 1] - self.arr_[row1][col2 + 1] - self.arr_[row2 + 1][col1] + self.arr_[row1][col1])
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)