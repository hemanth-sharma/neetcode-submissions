class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute Force [10,1,5,6,7,1]
        max_profit = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i+1, len(prices)):
                max_profit = max(max_profit, prices[j] - buy)
            
        return max_profit