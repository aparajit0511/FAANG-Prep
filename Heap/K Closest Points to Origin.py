class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        from collections import defaultdict
        hash_table = {}
        

        for point in points:
            dist = point[0] ** 2 + point[1] ** 2
            if dist in hash_table:
                hash_table[dist].append(point)
            else:
                hash_table[dist] = [point]

        hash_table = {key: value for key, value in sorted(hash_table.items(), key=lambda item: item[0])}
        # print(hash_table.values())
        result = [item for sublist in hash_table.values() for item in sublist]

        return result[:k]


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        import heapq
        from collections import defaultdict
        hash_table = defaultdict()
        heap = []

        for point in points:
            dist = point[0] ** 2 + point[1] ** 2
            dist = -1 * dist

            if len(heap) < k:
                heapq.heappush(heap,(dist,point))         
            elif dist > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap,(dist,point))

        first_items = [item[0] for item in heap]
        second_items = [item[1] for item in heap]

        return second_items



