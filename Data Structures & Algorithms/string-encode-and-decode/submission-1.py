class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = s.index("#", i)
            length = int(s[i:j])
            start = j + 1
            decoded.append(s[start:start + length])
            i = start + length
        return decoded