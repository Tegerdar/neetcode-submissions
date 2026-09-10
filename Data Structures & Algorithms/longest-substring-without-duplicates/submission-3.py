class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        ans = 0
        left = 0
        for i, c in enumerate(s):
            while c in substring:
                substring.remove(s[left])
                left += 1
            substring.add(c)
            ans = max(ans, len(substring))
        return ans