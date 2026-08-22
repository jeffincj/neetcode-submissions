class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r=defaultdict(list)
        for c in strs:
            alp=[0]*26
            for ch in c:
                alp[ord(ch)-ord('a')]+=1
            a=tuple(alp)
            if a in r:
                r[a].append(c)
            else:
                r[a]=[c]
        return list(r.values())