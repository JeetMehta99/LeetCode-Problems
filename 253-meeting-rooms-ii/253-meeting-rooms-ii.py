from operator import itemgetter
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # arr =[]
        # finishTime = sorted(intervals)
        # # print(finishTime)
        # for i in finishTime:
        #     # print(i[1])tt
        #     if arr == [] or arr[0] > i[0]:
        #         heapq.heappush(arr,i[1])
        #         # print(arr)
        #     else:
        #         heapq.heapreplace(arr,i[1])
        # return len(arr)
        first = itemgetter(0)
        second = itemgetter(1)
        start = sorted(intervals, key = first)
        end = sorted(intervals, key = second)
        print(start)
        print(end)
        res, count = 0, 0
        s, e = 0, 0
        while s < len(intervals):
            if start[s][0] < end[e][1]:
                count += 1
                s += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res
        