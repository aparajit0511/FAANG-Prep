class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()

        # print(intervals)

        for i in range(len(intervals)-1):
            pair = intervals[i]
            pair1 = intervals[i+1]
            # print(pair[1],pair1[0])
            if pair[1] > pair1[0]:
                return False

        return True