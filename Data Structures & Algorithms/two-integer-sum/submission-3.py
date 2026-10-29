class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for idx, val in enumerate(nums):
            complement = target - val
            if complement in h:
                return [h[complement], idx]
            h[val] = idx