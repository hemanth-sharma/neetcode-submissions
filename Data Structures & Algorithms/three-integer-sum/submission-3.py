class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # result = [].append(target)
        # nums=[-1,0,1,2,-1,-4]
        # [-4, -1, -1, 0, 1, 2]
        # sort the array
        # use two pointers to find target 
        nums.sort() 
        result = []
        for i, a in enumerate(nums): 
            if i > 0 and a == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right: 
                three_sum = a + nums[left] + nums[right]
                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    result.append([a, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        
        return result
            

        