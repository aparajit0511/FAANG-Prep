class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check columns
        for i in range(len(board)):
            visited = set()
            for j in range(9):
                if board[j][i] in visited and board[j][i] != '.':
                    return False
                visited.add(board[j][i])

        # Check rows
        for i in range(len(board[0])):
            visited = set()
            for j in range(9):
                if board[i][j] in visited and board[i][j] != '.':
                    return False
                visited.add(board[i][j])

        # Check each 3x3 block
        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):
                visited = set()
                for i in range(row_start, row_start + 3):
                    for j in range(col_start, col_start + 3):
                        if board[i][j] in visited and board[i][j] != '.':
                            return False
                        visited.add(board[i][j])

        return True
