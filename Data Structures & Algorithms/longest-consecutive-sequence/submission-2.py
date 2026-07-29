class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        longest = 0

        for i in range(len(nums)):
            if nums[i]-1 not in store:
                curr = 1
                while (nums[i] + curr) in store:
                    curr += 1
                longest = max(curr, longest)
        
        return longest