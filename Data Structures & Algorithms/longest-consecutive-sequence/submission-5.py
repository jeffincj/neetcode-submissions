class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums=sorted(set(nums))
        c=1
        s=1
        for i in range(len(nums)-1):
            if nums[i]+1==nums[i+1]:
                c+=1
                s=max(s,c)
            else: 
                c=1
        return s