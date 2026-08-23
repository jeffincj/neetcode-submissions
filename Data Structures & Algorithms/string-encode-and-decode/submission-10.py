class Solution:

    def encode(self, strs: List[str]) -> str:
        a=[]
        for s in strs:
            a.append(str(len(s)))
            a.append('#')
            a.append(s)
        return "".join(a)
    def decode(self, s: str) -> List[str]:
        i=0
        a=[]
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            l=int(s[i:j])
            i=j+1
            j=i+l
            a.append(s[i:j])
            i=j
        return a
