class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r=defaultdict(list)
        for c in strs:
            alp=[0]*26
            for ch in c:
                alp[ord(ch)-ord('a')]+=1
            if tuple(alp) in r:
                r[tuple(alp)].append(c)
            else:
                r[tuple(alp)]=[c]
        return list(r.values())