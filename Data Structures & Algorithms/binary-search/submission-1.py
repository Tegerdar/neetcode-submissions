class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # pointers for binary search
        r = len(nums) - 1
        l = 0
        while l <= r:
            if target == nums[l + (r - l) // 2]:
                return l + (r - l) // 2
            elif target > nums[l + (r - l) // 2]:
                l = l + (r - l) // 2 + 1
            else:
                r = l + (r - l) // 2 - 1
        return -1
            