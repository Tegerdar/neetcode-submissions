class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = [] # stack [index, temperature]
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                stackI, stackT = stack.pop()
                ans[stackI] = i - stackI
            stack.append([i, t])
        return ans