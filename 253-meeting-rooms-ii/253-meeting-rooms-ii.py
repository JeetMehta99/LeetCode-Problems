from operator import itemgetter
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        first = itemgetter(0)
        second = itemgetter(1)
        start = sorted(intervals, key = first)
        # print(start)
        end = sorted(intervals, key = second)
        # print(end)
        res, count, s, e = 0, 0, 0, 0
        while s < len(intervals):
            if start[s][0] < end[e][1]:
                count += 1
                s += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res
    