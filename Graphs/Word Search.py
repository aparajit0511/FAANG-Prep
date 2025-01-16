class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()
        
        def wordSearch(r,c,index):
            if index == len(word):
                return True
                
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index] or (r,c) in visited:
                return False   

            visited.add((r,c))
            res = wordSearch(r+1,c,index+1) or wordSearch(r-1,c,index+1) or wordSearch(r,c+1,index+1) or wordSearch(r,c-1,index+1) 
            visited.remove((r,c))

            return res


        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if wordSearch(i,j,0):
                        return True

        return False