class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=mv=0
        r=len(heights)-1
        while l<r:
            v=min(heights[l],heights[r])*(r-l)
            mv=max(mv,v)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return mv