class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r=defaultdict(list)
        for c in strs:
            s="".join(sorted(c))
            if s in r:
                r[s].append(c)
            else:
                r[s]=[c]
        return list(r.values())