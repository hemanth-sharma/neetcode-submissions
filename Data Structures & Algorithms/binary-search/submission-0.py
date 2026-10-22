class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        # for integer overflow in other langauges due to left + right
        # in python normal (left+right)//2 doesn't cause that issue because python allows arbitary large numbers. 
        while left <= right: 
            mid = left + (right-left)//2 
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid-1

        return -1    