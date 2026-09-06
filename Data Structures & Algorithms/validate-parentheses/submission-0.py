class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        pairs = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in pairs:
                if not brackets or brackets.pop() != pairs[c]:
                    return False
            else:
                brackets.append(c)
        return not brackets