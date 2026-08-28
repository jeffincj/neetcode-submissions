class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best=0
        w=prices[0]
        for r in range(1,len(prices)):
            if w>prices[r]:
                w=prices[r]
            elif prices[r]-w >0:
                best=max(best,prices[r]-w)
        return best