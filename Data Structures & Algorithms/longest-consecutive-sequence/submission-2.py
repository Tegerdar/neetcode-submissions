class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        for n in s:
            if n - 1 in s:
                continue
            length = 1
            while n + length in s:
                length += 1
            ans = max(ans, length)
        return ans