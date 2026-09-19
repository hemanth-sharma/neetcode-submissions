class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 1, 2, 3, [2  1  1] 3
        # 1, 2, 3,  2 [1  1  3]
        # if cur max is at i and j+1 is not greater than cur max
        # then we need a second max
        
        i, j = 0, k-1
        result = []
        current_max = max(nums[i:k]) # 2
        result.append(current_max)
        while j < len(nums):
            i += 1
            j += 1
            if j < len(nums) and current_max == nums[i-1] and current_max > nums[j]:
                # reset to second max
                current_max = max(nums[i:j+1])
            elif j < len(nums): 
                current_max = max(current_max, nums[j])
            if j < len(nums):
                result.append(current_max)
        return result
