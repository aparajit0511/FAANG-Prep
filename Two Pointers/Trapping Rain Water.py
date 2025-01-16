class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        
        for i in range(1,len(height)-1):
            left_max = 0
            right_max = 0
            for j in range(i,-1,-1):
                left_max = max(left_max,height[j])

            for k in range(i,len(height)):
                right_max = max(right_max,height[k])

            # print(left_max,right_max,height[i])

            result += min(left_max,right_max)-height[i]

        return result



class Solution:
    def trap(self, height: List[int]) -> int:
         
        result = 0

        left_max = [0] * len(height)
        right_max = [0] * len(height)

        for i in range(1,len(height)):
            left_max[i] = max(left_max[i-1],height[i-1])

        for j in range(len(height)-2,-1,-1):
            right_max[j] = max(right_max[j+1],height[j+1])

            ans = min(left_max[j],right_max[j]) - height[j]
            if ans > 0:
                result += ans

        return result