class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        r=len(s1)
        for l in range(len(s2)-(r-1)):
            if sorted(s1)==sorted(s2[l:l+r]):
                return True
        else:
            return False