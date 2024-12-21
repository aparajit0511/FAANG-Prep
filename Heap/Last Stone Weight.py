class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        

        while True:
            stones.sort()

            if len(stones) == 1:
                break

            val = stones[-1] - stones[-2]
            stones.pop()
            stones.pop()

            stones.append(abs(val))

        return stones[0]



class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        import heapq

        heap = []
        for num in stones:
            heap.append(num * -1)

        while True:

            heapq.heapify(heap)

            if len(heap) == 1:
                break

            stone1 = heapq.heappop(heap)
            stone2 = heapq.heappop(heap)

            val = abs((stone1 * -1) - (stone2 * -1))
            heapq.heappush(heap,val*-1)

        return heap[0]
