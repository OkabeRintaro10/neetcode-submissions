from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = defaultdict(list)
        for ele in strs:
            d[tuple(sorted(ele))].append(ele)
        return list(d.values())