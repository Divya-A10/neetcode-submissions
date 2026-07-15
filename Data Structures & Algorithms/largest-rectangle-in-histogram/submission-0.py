class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # stores indices
        maxArea = 0

        for i, h in enumerate(heights):

            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                maxArea = max(maxArea, height * width)

            stack.append(i)

        while stack:
            height = heights[stack.pop()]

            if stack:
                width = len(heights) - stack[-1] - 1
            else:
                width = len(heights)

            maxArea = max(maxArea, height * width)

        return maxArea
        