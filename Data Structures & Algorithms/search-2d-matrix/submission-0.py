class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_l, row_h = 0, len(matrix)-1

        while(row_l <= row_h):
            mid_row = row_l + ((row_h - row_l) // 2)
            col_l, col_h = 0, len(matrix[0])-1
            while(col_l <= col_h):
                mid_col = col_l + ((col_h - col_l) // 2)
                if(matrix[mid_row][mid_col] == target):
                    return True
                elif(matrix[mid_row][mid_col] < target):
                    col_l = mid_col + 1
                else:
                    col_h = mid_col - 1
            if(matrix[mid_row][0] < target):
                row_l = mid_row + 1
            else:
                row_h = mid_row - 1
        return False
                