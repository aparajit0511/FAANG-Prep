class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        result = float('inf')

        for i in range(len(nums)):
            sum = 0
            for j in range(i,len(nums)):
                sum += nums[j]

                if sum >= k:
                    result = min(result,j-i+1)
                    break

        return -1 if result == float('inf') else result



class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        from collections import deque
        queue = deque()

        cumSum = 0
        result = float('inf')

        for i in range(len(nums)):

            cumSum += nums[i]
            if cumSum >= k:
                result = min(result,i+1)
            queue.append((cumSum,i))


            while queue and cumSum - queue[0][1]>= k:
                item , value = queue.popleft()
                cumSum -= item
                

            while queue and cumSum < queue[-1][0]:
                queue.popleft()

        return -1 if result == float('inf') else result