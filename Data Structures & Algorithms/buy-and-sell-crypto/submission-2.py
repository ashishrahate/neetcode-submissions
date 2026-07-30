class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , r = 0, 1
        maxdiff= 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            elif prices[r] - prices[l] > maxdiff:
                maxdiff = prices[r] - prices[l]
            r += 1
        return maxdiff
            
        