class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        cnt = {n:0 for n in nums} # for duplicate nums
        for n in nums:
            cnt[n] += 1
        def dfs(): # backtracking
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for n in cnt:
                if cnt[n] > 0:
                    perm.append(n)
                    cnt[n] -= 1
                    
                    dfs()
                    cnt[n] += 1 # clean up
                    perm.pop() # remove val you ended up adding in perm.append()
        dfs()
        return res