class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            for j in range(i+1,len(temperatures)):

                if temperatures[j] > temperatures[i]:
                    result[i] = (j-i)
                    break

        return result


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0] * len(temperatures)

        stack = []
        stack.append(0)

        for i in range(1,len(temperatures)):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                result[stack[-1]] = i - stack[-1]
                stack.pop()

            stack.append(i)
            # print(stack,temperatures[i])

        return result