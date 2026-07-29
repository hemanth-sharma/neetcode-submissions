class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        result = [item[0] for item in sorted(count.items(), key=lambda a: a[1], reverse=True)[:k]]
        return result