class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        org = nums[:]

        self.checkPermutation(nums,org,0)

    def checkPermutation(self,nums,org,start):

        # if int("".join(map(str, nums))) > int("".join(map(str, org))):
        #     return 

        if start == len(nums) and int("".join(map(str, nums))) > int("".join(map(str, org))):
            print(int("".join(map(str, nums))))
            # print(int("".join(map(str, org))))
            # if int("".join(map(str, nums))) > int("".join(map(str, org))):
            #     return 
            return 

        for i in range(start,len(nums)):

            nums[start],nums[i] = nums[i],nums[start]
            self.checkPermutation(nums,org,start+1)
            nums[start],nums[i] = nums[i],nums[start]



from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        pivot1 = -1

        # Step 1: Find the first decreasing element from the right
        for i in range(len(nums) - 2, -1, -1):  # Start from second last element
            if nums[i] < nums[i + 1]:
                pivot1 = i
                break

        if pivot1 == -1:  # If no decreasing element is found, reverse the array
            nums.reverse()
            return

        # Step 2: Find the smallest element larger than nums[pivot1] to the right
        for i in range(len(nums) - 1, pivot1, -1):
            if nums[i] > nums[pivot1]:
                # Swap nums[pivot1] and nums[i]
                nums[pivot1], nums[i] = nums[i], nums[pivot1]
                break

        # Step 3: Reverse the subarray to the right of pivot1
        nums[pivot1 + 1:] = reversed(nums[pivot1 + 1:])
