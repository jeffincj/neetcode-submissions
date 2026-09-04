class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        if len(nums)<k:
            return res
        maxn=max(nums[0:k])
        res.append(maxn)
        l=1
        for r in range(k,len(nums),1):
            if maxn!=nums[l-1]:
                if nums[r]>maxn:
                    maxn=nums[r]
                    res.append(maxn)
                else:
                    res.append(maxn)
            else:
                maxn=max(nums[l:r+1])
                res.append(maxn)
            l+=1
        return res