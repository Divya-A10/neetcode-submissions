class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        cset = set()
        l = 0
        for r in range (len(s)):
            while s[r] in cset:
                cset.remove(s[l])
                l += 1
            cset.add(s[r])
            res = max(res, r- l + 1)
        return res
        