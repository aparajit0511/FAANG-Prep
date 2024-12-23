class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        start , end = 0 , len(nums)-1

        while start <= end:

            mid = (start + end) // 2

            if nums[mid] == nums[end]:
                break
            elif nums[mid] > nums[end]:
                start = mid + 1
            elif nums[mid] < nums[end]:
                end = mid - 1

        return mid