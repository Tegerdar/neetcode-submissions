class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [1] * length

        # ans[i] = product of nums[0...i-1]        
        prefix = 1
        for i in range(1, length):
            prefix *= nums[i-1]
            ans[i] = prefix

        # suffix = product of nums[i+1...length-1]; ans[i] - final answer
        suffix = 1
        for i in range(length-2, -1, -1):
            suffix *= nums[i+1]
            ans[i] *= suffix

        return ans