class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        value = 1
        zero_cnt = 0
        for n in nums:
            if n == 0:
                zero_cnt +=1
                if zero_cnt == 2:
                    return [0] * length
            else:
                value *= n
        if zero_cnt == 1:
            ans = [0 for _ in range(length)]
            ans[nums.index(0)] = value
            return ans
        ans = [value for _ in range(length)]
        for i in range(length):
            ans[i] //= nums[i]
        return ans