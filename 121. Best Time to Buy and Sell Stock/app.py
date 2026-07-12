class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for sell in prices[1:]:
            if sell > buy:
                profit = max(profit, sell - buy)
            else:
                buy = sell
        return profit

print(Solution().maxProfit([7,1,5,3,6,4]))

