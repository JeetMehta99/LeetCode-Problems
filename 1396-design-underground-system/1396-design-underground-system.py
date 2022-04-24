class UndergroundSystem:

    def __init__(self):
        # cust_id = (starttime, init_station)
        self.h1 = defaultdict(tuple)
         # start,end = end_time - start_time
        self.h2 = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.h1[id] = (t, stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        init_time, init_station = self.h1[id]
        total = t - init_time
        self.h2[(init_station, stationName)].append(total)
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.h2[(startStation,endStation)])/len(self.h2[(startStation, endStation)])
        
# https://www.youtube.com/watch?v=AXMSHVedysk

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)