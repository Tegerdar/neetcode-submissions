class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        res = 0

        for num in nums:
            if not mp[num]:
                right = mp[num + 1]
                left = mp[num - 1]
                mp[num] = left + right + 1
                mp[num - left] = mp[num]
                mp[num + right] = mp[num]
                res = max(res, mp[num])
        return res