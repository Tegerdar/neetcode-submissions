class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        ans = 0
        max_count = 0
        seen = {}
        for r in range(len(s)):
            if s[r] in seen:
                seen[s[r]] += 1
            else:
                seen[s[r]] = 1
            max_count = max(seen.values())
            while (r - l - max_count + 1) > k:
                seen[s[l]] -= 1
                l += 1
                max_count = max(seen.values())
            ans = max(r - l + 1, ans)
        return ans