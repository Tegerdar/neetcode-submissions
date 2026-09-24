class Solution:
    # encoding strings by using length of string separated by '+'
    def encode(self, strs: List[str]) -> str:
        return "".join(str(len(s)) + "+" + s for s in strs)
    def decode(self, s: str) -> List[str]:
        strs = []
        length_of_word = -1
        i = 0
        while i < len(s) or length_of_word >= 0:
            if length_of_word == -1:
                length_of_word = 0
                while s[i] != "+":
                    length_of_word = length_of_word * 10 + int(s[i])
                    i += 1
                i += 1
            else:
                strs.append("".join(s[i:length_of_word + i]))
                i += length_of_word
                length_of_word = -1
        return strs