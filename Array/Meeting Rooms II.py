class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        start = [i[0] for i in intervals]
        end = [i[1] for i in intervals]

        start.sort()
        end.sort()

        print("start",start,"end",end)

        s , e = 0 ,0 
        result , count = 0 , 0

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1

            result = max(result,count)

        return result