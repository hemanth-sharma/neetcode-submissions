class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # # find row 
        # l, r = 0, len(matrix)-1
        # correct_row = -1
        # while l <= r:
        #     m = l + (r-l)//2
        #     if matrix[m][0] == target:
        #         return True
        #     if matrix[m][0] < target:
        #         correct_row = m
        #         l = m+1
        #     else:
        #         r = m-1
        # if correct_row == -1:
        #     return False

        # # find column
        # l, r = 0, len(matrix[correct_row])-1
        # while l <= r:
        #     m = l + (r-l)//2
        #     if matrix[correct_row][m] == target:
        #         return True
        #     elif matrix[correct_row][m] < target:
        #         l = m+1
        #     else:
        #         r = m-1

        # return False
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLS - 1
        while l <= r:
            m = l + (r - l) // 2
            row, col = m // COLS, m % COLS
            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True
        return False