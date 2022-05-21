class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [0] * (amount + 1)
        # print(dp)
        for i in range(1, len(dp)):
            combs = []
            for x in coins:
                if i - x < 0:
                    continue
                if dp[i - x] == -1:
                    continue
                combs.append(dp[i - x] + 1)
            if len(combs) == 0:
                dp[i] = -1
            else:
                dp[i] = min(combs)
        return dp[len(dp) - 1]