class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        row_call = [set() for _ in range(n)]
        col_call = [set() for _ in range(n)]
        square_call = [set() for _ in range(n)]
        for row in range(n):
            for col in range(n):
                num = board[row][col]
                if not num.isdigit():
                    continue
                square_index = (row // 3) * 3 + (col // 3)
                if num in row_call[row] or num in col_call[col] or num in square_call[square_index]:
                    return False
                else:
                    row_call[row].add(num)
                    col_call[col].add(num)
                    square_call[square_index].add(num)
        return True 
        