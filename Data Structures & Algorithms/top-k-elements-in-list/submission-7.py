class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=Counter(nums)
        top_two=[i for i, r in res.most_common(k)]
        return top_two
