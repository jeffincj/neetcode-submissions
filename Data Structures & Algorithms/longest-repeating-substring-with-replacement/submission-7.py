class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=res=maxC=0
        c=defaultdict(int)
        for r in range(len(s)):
            c[s[r]]+=1
            maxC=max(maxC,c[s[r]])
            if (r-l+1)-maxC>k:
                c[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res