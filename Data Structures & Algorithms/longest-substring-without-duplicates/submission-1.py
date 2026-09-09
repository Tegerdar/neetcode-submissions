class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        ans = 0
        left = 0
        for i, c in enumerate(s):
            left = max(left, 1 + seen.get(c, -1))
            seen[c] = i
            ans = max(ans, i - left + 1)
        return ans