class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums[j] = target - nums[i]
        for i in range(len(nums)):
            try:
                j = nums.index(target-nums[i])
                if i == j:
                    continue
                elif i > j:
                    return [j, i]
                elif i < j:
                    return [i, j]
            except:
                continue