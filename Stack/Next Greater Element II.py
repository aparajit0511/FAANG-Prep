class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        count = len(nums)*2
        i = 0
        result = [-1] * len(nums)
        stack = []

        while count > 0:

            i = i % len(nums)
            while stack and nums[i] > nums[stack[-1]]:
                result[stack[-1]] = nums[i]
                stack.pop()

            stack.append(i)
            i = i+1
            count -= 1

        return result



class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)
        n = len(nums)
        stack = []

        for i in range(2 * n - 1, -1, -1):  # Start from the end
            while stack and nums[stack[-1]] <= nums[i % n]:
                stack.pop()  # Pop elements that are less than or equal to the current value

            if stack:  # If the stack is not empty, the top is the next greater element
                result[i % n] = nums[stack[-1]]

            stack.append(i % n)  # Push the current index (mod n for circular behavior)

        return result
