class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        count = 0
        max_count = 0
        # print(nums)

        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 0:
                continue
            if nums[i+1] - nums[i]  == 1:
                count += 1
            else:
                count = 0

            max_count = max(max_count,count)

        return max_count+1
        


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        max_count = 0

        for num in nums:
            if num-1 not in nums:
                prevNum = num

                while prevNum in nums:
                    prevNum += 1
                    max_count = max(max_count,prevNum-num)

        return max_count