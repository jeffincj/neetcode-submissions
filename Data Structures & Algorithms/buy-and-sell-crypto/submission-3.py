class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best=0
        minPrice=prices[0]
        for r in range(1,len(prices)):
            minPrice=min(minPrice,prices[r])
            best=max(best,prices[r]-minPrice)
        return best