class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_price = 0
        smallest = prices[0]
        for price in prices:
            best_price = max(best_price, price - smallest)
            smallest = min(smallest, price)
        return best_price


        