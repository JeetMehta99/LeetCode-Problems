class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)
        dp = [[0 for _ in range(n)] for _ in range(m)]
        if obstacleGrid[0][0] == 1 or m==0:
            return 0
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i>0:
                    if obstacleGrid[i][j] != 1:
                        dp[i][j] += dp[i-1][j]
                        # print(dp)
                if j>0:
                    if obstacleGrid[i][j] != 1:
                        dp[i][j] += dp[i][j-1]
                        # print(dp)
                        
        return dp[m-1][n-1]

        