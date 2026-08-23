class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset=set(nums)
        res=0
        for num in nset:
            if num-1 not in nset:
                c=1
                while num+c in nset:
                    c+=1
                res=max(res,c)
        return res