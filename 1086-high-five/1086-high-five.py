import heapq
from collections import defaultdict

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        
        cache = defaultdict(list)
        
        for s_id, score in items:
            if(len(cache[s_id])) < 5:
                heapq.heappush(cache[s_id], score)
            else:
                heapq.heappushpop(cache[s_id], score)
        
        res = []
        for s_id, score in cache.items():
            avg = sum(score) // len(score)
            res.append((s_id, avg))
        
        return sorted(res)
