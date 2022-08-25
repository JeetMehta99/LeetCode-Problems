class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 0 
        max = 0
        while j < len(prices):
            profit = prices[j] - prices[i]
            if profit >= max:
                j += 1
                max = profit
            elif profit <= 0:
                i = j
                j += 1
            elif 0 < profit < max:
                j += 1
        return max

        