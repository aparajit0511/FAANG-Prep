class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        start , end = 0 , len(matrix)-1

        while start <= end:
            mid = (start + end) // 2

            if matrix[mid][0] == target:
                return True
            elif target < matrix[mid][0]:
                end = mid - 1
            else:
                start = mid + 1


        start , end = 0 , len(matrix[0])-1
        row = end

        while start <= end:
            mid = (start + end) // 2

            if matrix[row][mid] == target:
                return True
            elif target < matrix[row][mid]:
                end = mid - 1
            else:
                start = mid + 1


        return False