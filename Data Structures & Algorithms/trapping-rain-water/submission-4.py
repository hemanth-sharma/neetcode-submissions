class Solution:
    def trap(self, height: List[int]) -> int:
        # find max left height and then max right height and take min reminder.
        # maxleft - h[i] and maxright - h[i] (ignore -ve)
        i, j = 0, len(height)-1
        maxLeft, maxRight = height[i], height[j]
        max_water = 0
        # height=[0,1,0,2,1,0,1,3,2,1,2,1]
        #                       i j
        #         0 0 1 0 1 2 1 0 0 1 0 0 = 6
        while i < j:
            if maxLeft <= maxRight:
                i += 1
                maxLeft = max(maxLeft, height[i])
                water = (maxLeft - height[i])
                max_water += water
            else:
                j -= 1
                maxRight = max(maxRight, height[j])
                water = (maxRight - height[j])
                max_water += water

        return max_water


        