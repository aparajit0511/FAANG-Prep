class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        top = 0
        down = len(matrix)-1
        right = len(matrix[0])-1
        left = 0

        result = []
        direction = 0

        while top <= down and left <= right:

            if direction == 0:

                for k in range(left,right+1):
                    result.append(matrix[top][k])

                print(result)

                top += 1

            elif direction == 1:

                for k in range(top,down+1):
                    result.append(matrix[k][right])

                print(result)

                right -= 1

            elif direction == 2:

                for k in range(right,left-1,-1):
                    result.append(matrix[down][k])

                print(result)

                down -= 1

            elif direction == 3:

                for k in range(down,top-1,-1):
                    result.append(matrix[k][left])

                print(result)

                left += 1

            direction = (direction + 1) % 4

        return result
