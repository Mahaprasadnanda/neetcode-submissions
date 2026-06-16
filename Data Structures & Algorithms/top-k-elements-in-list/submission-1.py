from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Hashmap=Counter(nums)
        topk=[key for key,value in Hashmap.most_common(k)]
        return topk
        