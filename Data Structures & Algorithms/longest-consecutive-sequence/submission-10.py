class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        nums.sort()
        count=c=1
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                continue
            elif nums[i]+1==nums[i+1]:
                c+=1
            else:
                count=max(count,c)
                c=1
            count=max(count,c)
        return count  