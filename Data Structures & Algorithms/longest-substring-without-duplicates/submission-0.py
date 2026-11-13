class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hset = {}
        left = 0 
        max_len = 0
        for right, c in enumerate(s):
            if c in hset and hset[c] >= left: left = hset[c] + 1
            hset[c] = right
            max_len = max(max_len, right-left + 1)
        return max_len