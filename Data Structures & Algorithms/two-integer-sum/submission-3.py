class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s= {}
        for i, num in enumerate(nums):
            d=target-num
            if d in s:
                return [s[d],i]
            s[num]=i