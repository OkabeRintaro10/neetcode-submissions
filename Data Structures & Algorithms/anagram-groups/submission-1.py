from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = defaultdict(list)
        for idx, ele in enumerate(strs):
            # Looping through ele and adding string data to it indices
            lex_sort = ''.join(sorted(ele))
            d[lex_sort].append(ele)
        return list(d.values())