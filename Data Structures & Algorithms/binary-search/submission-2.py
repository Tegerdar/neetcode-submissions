class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # pointers for binary search
        r = len(nums) - 1
        l = 0
        while l <= r:
            middle = l + (r - l) // 2
            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                l = middle + 1
            else:
                r = middle - 1
        return -1
            