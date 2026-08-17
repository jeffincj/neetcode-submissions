class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        o=[]
        pr,po=1,1
        for i in range(len(nums)):
            o.append(pr)
            pr*=nums[i]
        for i in range(len(nums)-1,-1,-1):
            o[i]*=po
            po*=nums[i]
        return o[0:len(nums)]