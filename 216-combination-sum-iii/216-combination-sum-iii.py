class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        # dfs
        def dfs(stack, num, curSum):
            if len(stack) == k:
                if curSum == n:
                    res.append(stack)
                return
            
            for i in range(num, 10):
                if curSum+i>n:
                    break
                dfs(stack+[i], i+1, curSum+i)
                
        dfs([], 1, 0)
        return res