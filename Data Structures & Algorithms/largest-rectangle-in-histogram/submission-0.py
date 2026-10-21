class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        n = len(heights)
        # i = length
        # height[i] = width
        # area = length * breadth 
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                top_index, top_height = stack.pop()
                area = max(area, top_height * (i-top_index))
                start = top_index
            stack.append((start, h))

        for i, h in stack:
            area = max(area, h * (n-i))
        
        return area


                



