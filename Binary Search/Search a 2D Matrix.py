class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                if matrix[i][j] == target:
                    return True

        return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        for i in range(len(matrix)):
            left , right = i , len(matrix[i])-1
            print(left,right)
            print("hi")

            while left <= right:
                mid = (left + right) // 2
                print(left,right,mid)

                if matrix[i][mid] == target:
                    return True
                elif target < matrix[i][mid]:
                    right = mid - 1
                elif target> matrix[i][mid] :
                    left = mid + 1

                print(left,right,mid)


        for j in range(len(matrix[0])):
            left ,right = j , len(matrix[0])-1

            while left <= right:
                if matrix[i][mid] == target:
                    return True
                elif target < matrix[i][mid]:
                    right = mid - 1
                elif target> matrix[i][mid] :
                    left = mid + 1


        return False