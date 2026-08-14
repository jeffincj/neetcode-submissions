class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        f = [[] for _ in range(len(nums) + 1)]
        for i in nums:
            count[i]=1+count.get(i,0)
        for i,cn in count.items():
            f[cn].append(i)
        res=[]
        for i in range(len(f) - 1, 0, -1):
            for num in f[i]:
                res.append(num)
                if len(res) == k:
                    return res

        