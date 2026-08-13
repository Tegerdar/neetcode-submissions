from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]
        for n, f in count.items():
            buckets[f].append(n)
        ans = []
        for i in range(len(nums), 0, -1):
            for n in buckets[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans
        return ans