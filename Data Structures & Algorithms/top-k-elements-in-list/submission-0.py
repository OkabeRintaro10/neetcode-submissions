from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Create a hash map
        h = defaultdict(int)
        # Iterate through the list of nums
        for n in nums:
            # add the key and value to a dict
            h[n] += 1
        # # fetch the keys equivalent to the k value
        return sorted(h.keys(), key=lambda x: h[x], reverse=True)[:k]