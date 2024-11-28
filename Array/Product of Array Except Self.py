class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = []

        for i in range(len(nums)):
            pro = 1
            for j in range(len(nums)):
                if i == j:
                    continue

                pro = pro * nums[j]

            result.append(pro)

        return result



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left = [1] * len(nums)
        right = [1] * len(nums)

        for i in range(1,len(nums)):
            left[i] = nums[i-1] * left[i-1]

        for i in range(len(nums)-2,-1,-1):
            right[i] = nums[i+1] * right[i+1]

        for i in range(len(left)):
            left[i] *= right[i]

        return left