class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        ans = []
        length = len(nums)
        for i, n in enumerate(nums):
            count[n] -= 1
            if i and n == nums[i - 1]:
                continue
            for j in range(i + 1, length):
                n_j = nums[j]
                count[n_j] -= 1
                if j - 1 > i and n_j == nums[j - 1]:
                    continue
                target = -(n + n_j)
                if count[target] > 0:
                    ans.append([n, n_j, target])
            for j in range(i + 1, length):
                count[nums[j]] += 1
        return ans