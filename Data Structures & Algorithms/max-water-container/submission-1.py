class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # max_water = 0
        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         max_water = max(max_water, min(heights[i], heights[j]) * (j-i))
            
        # return max_water
        max_water = 0
        i, j = 0, len(heights)-1
        while(i < j):
            max_water = max(min(heights[i], heights[j]) * (j-i), max_water)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return max_water