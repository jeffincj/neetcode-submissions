class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        co=c=0
        s=set(nums)
        for num in s:
            if num-1 not in s:
                c=1
                while num+c in s:
                    c+=1
                co=max(co,c)
        return max(co,c)