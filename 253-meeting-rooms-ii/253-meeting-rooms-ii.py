class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        arr =[]
        finishTime = sorted(intervals)
        # print(finishTime)
        for i in finishTime:
            # print(i[1])tt
            if arr == [] or arr[0] > i[0]:
                heapq.heappush(arr,i[1])
                # print(arr)
            else:
                heapq.heapreplace(arr,i[1])
        return len(arr)
        