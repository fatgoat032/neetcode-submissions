class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mat = [x for row in matrix for x in row]
        first = 0
        last = len(mat) - 1
        while last >= first:
            mid = (first + last) // 2
            if mat[mid] == target:
                return True
            elif mat[mid] > target:
                last = mid - 1
            elif mat[mid] < target:
                first = mid + 1
        return False
        