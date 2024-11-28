class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        for i in range(len(nums)):

            if nums[i] == target:
                return i

        return -1



class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 1 and nums[0] == target:
            return 0
        
        left,right = 0,len(nums)-1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        print(left)


        if nums[left] == target:
            return left

        pivot = left

        left , right = 0, len(nums)-1

        if target >= nums[pivot] and target <= nums[right]:
            left = pivot 
        else:
            right = pivot-1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return -1