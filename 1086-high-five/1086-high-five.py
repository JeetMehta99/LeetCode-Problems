import heapq
from collections import defaultdict

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        
        cache = defaultdict(list)  # {student_id: [top-5 scores]}
	
        for student_id, score in items:
            if len(cache[student_id]) < 5:  
                heapq.heappush(cache[student_id], score)
            else:
                heapq.heappushpop(cache[student_id], score)

        ans = []
        for student_id, scores in cache.items():
            average = sum(scores) // len(scores)
            ans.append((student_id, average))

        return sorted(ans)