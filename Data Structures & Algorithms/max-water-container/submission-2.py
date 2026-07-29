class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # [1,7,2,5,4,7,3,6]
        #  i             j
        #  calculate water = min(1, 6) = 2 * (8-1) = 1 * 7
        #  calculate water formula = min(nums[i], nums[j]) * (j-i)
        #  
        i, j = 0, len(heights)-1
        max_water = 0
        while i < j:
            max_water = max(min(heights[i], heights[j]) * (j-i), max_water)
            if heights[i] <= heights[j]:
                i += 1
            elif heights[i] > heights[j]:
                j -= 1
        
        return max_water
