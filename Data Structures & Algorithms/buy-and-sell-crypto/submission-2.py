class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best=0
        l=0
        for r in range(1,len(prices)):
            if prices[l]>prices[r]:
                l=r
            elif prices[r]-prices[l]>0:
                best=max(best,prices[r]-prices[l])
        return best