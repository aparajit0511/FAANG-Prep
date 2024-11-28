class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        unique = set()
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    sum = nums[i] + nums[j] + nums[k]

                    if sum == 0:
                        unique.add((nums[i],nums[j],nums[k]))

        return list(unique)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        unique = set()

        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1

            while(left < right):
                sum = nums[i] + nums[left] + nums[right]
                left += 1
                right -= 1

                if sum == 0:
                    unique.add((nums[i],nums[left],nums[right]))
                elif sum < 0:
                    right = right - 1
                else:
                    left = left + 1

        return list(unique)