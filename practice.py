class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        path = set()
        
        def wordSearch(r,c,index):
            if index == len(word):
                return True

            if r < 0 or r >= row or c < 0 or c >= col or board[r][c] != word[index] or (r,c) in path:
                return False

            path.add((r,c))
            res = wordSearch(r+1,c,index+1) or wordSearch(r-1,c,index+1) or wordSearch(r,c+1,index+1) or wordSearch(r,c-1,index+1)

            path.remove((r,c))

            return res


        for i in range(row):
            for j in range(col):
                index = 0

                if board[i][j] == word[index]:
                    if wordSearch(i,j,index):
                        return True

        return False

