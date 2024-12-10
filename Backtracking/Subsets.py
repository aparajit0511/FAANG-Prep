class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        # result.append([])

        def backtrack(nums,combination,result):

            result.append(combination[:])


            for i in range(len(nums)):
                combination.append(nums[i])
                result = backtrack(nums[i+1:],combination,result)
                combination.pop()

            return result

        return backtrack(nums,[],result)