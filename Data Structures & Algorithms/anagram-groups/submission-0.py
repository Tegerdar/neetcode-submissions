class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:  
        ans = {}
        for s in strs:
            key = [0]*26
            for c in s:
                key[ord(c)-ord('a')] = key[ord(c)-ord('a')]+1
            key = tuple(key)
            if key in ans:
                ans[key].append(s)
            else:
                ans[key] = [s]
        return list(ans.values())
            