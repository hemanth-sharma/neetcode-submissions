class Solution:
    def binary_search(self, left, right, nums, target):
        if left > right:
            return -1
        mid = left + (right-left)//2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            return self.binary_search(mid+1, right, nums, target)
        else: 
            return self.binary_search(left, mid-1, nums, target)
        
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(0, len(nums)-1, nums, target)
        
        # for integer overflow in other langauges due to left + right
        # in python normal (left+right)//2 doesn't cause that issue because python allows arbitary large numbers. 
        # while left <= right: 
        #     mid = left + (right-left)//2 
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] < target:
        #         left = mid+1
        #     elif nums[mid] > target:
        #         right = mid-1

        # return -1    
        ## recursive
        
        