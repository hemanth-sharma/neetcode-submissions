class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = 1, 1
        left_output = [1] * len(nums)
        right_output = [1] * len(nums) # Final result
        
        # Left
        for i in range(1, len(nums)):
            prefix *= nums[i - 1]
            left_output[i] = prefix
        
        # Right
        for i in range(len(nums) - 2, -1, -1):
            suffix *= nums[i + 1]
            right_output[i] = suffix * left_output[i]
        
        right_output[-1] = left_output[-1]
        return right_output
        