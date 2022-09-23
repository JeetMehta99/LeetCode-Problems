class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        diff_arr = []
        for a, b in costs:
            diff_arr.append([b-a, a, b])
        
        diff_arr.sort()
        ans = 0
        for i in range(len(diff_arr)):
            if i < ( len(diff_arr) // 2):
                ans += diff_arr[i][2]
            else:
                ans += diff_arr[i][1]
        return ans 
            