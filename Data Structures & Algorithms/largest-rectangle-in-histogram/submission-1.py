class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # stack
        ans = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                popped_start, curH = stack.pop()
                ans = max((i - popped_start) * curH, ans)
                start = popped_start
            stack.append([start, h]) 

        while stack:
            start, curH = stack.pop()
            ans = max((len(heights) - start) * curH, ans)
        return ans