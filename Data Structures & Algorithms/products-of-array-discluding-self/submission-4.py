class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count_zero = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count_zero += 1
            else:
                product *= nums[i]
        
        for i in range(len(nums)):
            if count_zero == 0:
                nums[i] = product//nums[i]
            elif count_zero == 1:
                if nums[i] == 0:
                    nums[i] = product
                else:
                    nums[i] = 0
            elif count_zero > 1:
                nums[i] = 0

        return nums