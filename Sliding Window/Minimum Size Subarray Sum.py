class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = float('inf')
        
        for i in range(len(nums)):
            sum = 0
            for j in range(i,len(nums)):
                sum += nums[j]

                if sum >= target:
                    # print(j,i,nums[j],nums[i],sum)
                    result = min(result,j-i+1)
                    break

        return 0 if result == float('inf') else result




class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        result = float('inf')
        start = 0
        sum = 0

        for i in range(len(nums)):
            sum += nums[i]

            while sum >= target:
                result = min(result,i-start+1)
                sum -= nums[start]
                start += 1

        return 0 if result == float('inf') else result
