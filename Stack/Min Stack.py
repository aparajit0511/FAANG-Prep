class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return  self.stack[-1]
        

    def getMin(self) -> int:
        return min(self.stack)
        



class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = [float("inf")]
        

    def push(self, val: int) -> None:
        if self.min_stack[-1] >= val:
            self.min_stack.append(val)
       
        self.stack.append(val)

    def pop(self) -> None:
        item = self.stack.pop()
        if item == self.min_stack[-1]:
            self.min_stack.pop()
        

    def top(self) -> int:
        return  self.stack[-1]
        

    def getMin(self) -> int:
        
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()