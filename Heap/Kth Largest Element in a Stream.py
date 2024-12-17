from heapq import heappush, heappushpop, heapify
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # Take the first k elements and heapify
        self.heap = nums[:k]
        heapify(self.heap)  # Turns the first k elements into a min-heap

        # Add remaining elements one by one
        for num in nums[k:]:
            heappushpop(self.heap, num)

    def add(self, val: int) -> int:
        # If heap has less than k elements, add directly
        if len(self.heap) < self.k:
            heappush(self.heap, val)
        else:
            # Push the new value and pop the smallest to maintain k elements
            heappushpop(self.heap, val)
        
        # The smallest element in the heap is the kth largest
        return self.heap[0]
