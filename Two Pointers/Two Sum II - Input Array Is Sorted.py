class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_table = {}

        for i in range(len(nums)):

            if nums[i] not in hash_table:
                hash_table[target-nums[i]] = i+1
            else:
                return [hash_table[nums[i]],i+1]



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        left , right = 0 , len(nums)-1

        while left < right:
            sum = nums[left] + nums[right]

            if sum == target:
                return [left+1,right+1]
            elif target < sum:
                right -= 1
            else:
                left += 1
