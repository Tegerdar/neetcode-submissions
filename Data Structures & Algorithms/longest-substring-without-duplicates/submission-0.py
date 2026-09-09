class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        ans = 0
        start = 0
        for i, c in enumerate(s):
            while c in seen:
                seen.remove(s[start])
                start += 1
            seen.add(c)
            ans = max(ans, len(seen))
        return ans