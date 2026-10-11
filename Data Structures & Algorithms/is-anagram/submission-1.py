class Solution:
    def isAnagram(self, s: str, t: str):
        if len(s) != len(t):
            return False
        for i, j in zip(sorted(s), sorted(t)):

            if i != j:
                return False
        return True