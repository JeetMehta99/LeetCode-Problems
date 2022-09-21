class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row = len(mat)
        col = len(mat[0])
        nums = [[] for _ in range(row+col-1)]
        
        for r in range(row):
            for c in range(col):
                nums[r+c].append(mat[r][c])
        
        res = []
        for i in range(row+col-1):
            if i % 2 == 0:
                res.extend(nums[i][::-1])
            else:
                res.extend(nums[i])
        return res