class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):

                if nums[i] == nums[j]:
                    return True

        return False



class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        visited = set()

        for i in range(len(nums)):
            if nums[i] in visited:
                return True

            visited.add(nums[i])

        return False

