class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i+1, len(prices)):
                profit = prices[j] - buy
                result = max(result, profit)

        return result

        