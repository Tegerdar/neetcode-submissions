class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        for t in tokens:
            if t in operators:
                n1 = int(stack.pop())
                n2 = int(stack.pop())
                if t == "+":
                    stack.append(n2 + n1)
                elif t == "*":
                    stack.append(n2 * n1)
                elif t == "-":
                    stack.append(n2 - n1)
                else:
                    stack.append(int(n2 / n1)) # truncation towards zero
            else:
                stack.append(t)
        return int(stack.pop())