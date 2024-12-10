class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        maxArea = 0

        left , right = 0 , len(height)-1

        while left < right:

            if height[left] <= height[right]:
                area = height[left] * ((right-left))
                left += 1
            else:
                area = height[right] * ((right - left))
                right -= 1

            maxArea = max(area,maxArea)

        return maxArea