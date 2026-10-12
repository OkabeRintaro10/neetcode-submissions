from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = defaultdict(list)
        for ele in strs:
            count = [0] * 26
            for c in ele:
                count[ord(c) - ord('a')] +=1
            d[tuple(count)].append(ele)
        return list(d.values())