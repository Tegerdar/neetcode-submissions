class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ("+", "-", "/", "*")
        result = 0
        for t in tokens:
            if t in operators:
                x_l = stack.pop()
                x_r = stack.pop()
                if t == "+":
                    stack.append(x_r + x_l)
                elif t == "-":
                    stack.append(x_r - x_l)
                elif t == "*":
                    stack.append(x_r * x_l)
                else:
                    stack.append(int(x_r / x_l))
            else:
                stack.append(int(t))
        return stack[0]