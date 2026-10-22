from collections import defaultdict
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hmap = defaultdict(list)
        if len(numbers) < 2:
            return []
        for idx in range(len(numbers)):
            complement = target - numbers[idx]
            if hmap[complement] and hmap[complement][0] < idx:
                return [hmap[complement][0] + 1, idx + 1]

            hmap[numbers[idx]].append(idx)