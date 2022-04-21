class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        r, c = len(grid), len(grid[0])
        
        k = k % (r*c) # no. of rotations

        if k:
            temp = []
            i = ((r*c)-k)//c 
            j = ((r*c)-k)%c
            while k:
                if j==c:
                    i+=1
                    j=0
                temp.append(grid[i][j])
                j+=1
                k-=1
            pos = 0

            for i in range(0, r):
                for j in range(0, c):
                    temp.append(grid[i][j])
                    grid[i][j] = temp[pos] #rotation
                    pos+=1
        return grid
        