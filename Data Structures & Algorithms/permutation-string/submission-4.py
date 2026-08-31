from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n,m=len(s1),len(s2)
        if m<n: return False

        need=Counter(s1)
        window=Counter(s2[:n])
        if need==window: return True

        for r in range(n,m):
            window[s2[r]]+=1
            window[s2[r-n]]-=1
            if window[s2[r-n]] ==0: del window[s2[r-n]]
            if window==need: return True
        return False
