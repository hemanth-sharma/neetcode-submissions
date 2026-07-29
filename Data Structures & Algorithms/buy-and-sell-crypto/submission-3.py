class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Optimal Method
        max_profit = 0
        min_buy = prices[0]
        for sell in prices: 
            max_profit = max(max_profit, sell - min_buy)
            min_buy = min(min_buy, sell)
        
        return max_profit
        # # Brute Force [10,1,5,6,7,1]
        # max_profit = 0
        # for i in range(len(prices)):
        #     buy = prices[i]
        #     for j in range(i+1, len(prices)):
        #         max_profit = max(max_profit, prices[j] - buy)
            
        # # return max_profit

        # # Two Pointers 
        # max_profit = 0
        # l, r = 0, 1
        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         profit = prices[r] - prices[l] # sell - buy
        #         max_profit = max(max_profit, profit)
        #     else:
        #         l = r
        #     r += 1
        # # return max_profit