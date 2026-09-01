class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=='': return ""
        
        wind,tco={},{}
        for c in t:
            tco[c]=tco.get(c,0)+1
        have,need=0,len(tco)
        l=0
        res,resl=[-1,-1],float("infinity")
        for r in range(len(s)):
            c=s[r]
            wind[c]=wind.get(c,0)+1
            if c in tco and wind[c]==tco[c]:
                have+=1
            while have == need:
                if r-l+1 < resl:
                    res=[l,r]
                    resl=r-l+1
                wind[s[l]]-=1
                if s[l] in tco and wind[s[l]]<tco[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if resl != float("infinity") else ""
