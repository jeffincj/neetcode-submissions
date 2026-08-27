class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        ML=height[l]
        MR=height[r]
        res=0
        while l<r:
            if ML<=MR:
                l+=1
                ML=max(ML,height[l])
                res+=ML-height[l]
            else:
                r-=1
                MR=max(MR,height[r])
                res+=MR-height[r]
        return res