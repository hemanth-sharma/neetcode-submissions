class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = {} # O(n) space
        longest_sq = 0
        for i in nums:
            hashmap[i] = i
        # [0,3,2,5,4,6,1,1]
        # [10,20,2,4,3,4,5]
        for i in range(len(nums)): 
            if nums[i]-1 not in hashmap:
                curr_sq = 1
                temp = nums[i]
                while temp+1 in hashmap: 
                    curr_sq += 1
                    temp += 1
                longest_sq = max(longest_sq, curr_sq)

        return longest_sq  
                
        
            

            