class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(nums,start,result):

            if start == len(nums):
                result.append(nums[:])
                return result

            for i in range(start,len(nums)):

                nums[start] , nums[i] = nums[i] , nums[start]

                result = backtrack(nums,start+1,result)

                nums[start] , nums[i] = nums[i] , nums[start]

            return result

        return backtrack(nums,0,[])
