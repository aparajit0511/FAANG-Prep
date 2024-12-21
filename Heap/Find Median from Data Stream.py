class MedianFinder:

    def __init__(self):
        self.nums = []
        

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        

    def findMedian(self) -> float:
        self.nums.sort()
        length = len(self.nums) // 2
        if len(self.nums) % 2 == 1:
            return self.nums[length]

        mid = self.nums[length]
        Lmid = self.nums[length-1]

        return (mid + Lmid) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

import heapq
class MedianFinder:

    def __init__(self):
        self.nums = []
        self.small , self.large = [] , []
        

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large,num)
        else:
            heapq.heappush(self.small,num * -1)

        if len(self.small) > len(self.large)+1:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large,val*-1)
        elif len(self.large) > len(self.small)+1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small,val * -1)


    def findMedian(self) -> float:

        if len(self.small) == len(self.large):
            return ((self.small[0] * -1 ) + self.large[0]) / 2

        if len(self.small) > len(self.large):
            return self.small[0] * -1

        else:
            return self.large[0]
        