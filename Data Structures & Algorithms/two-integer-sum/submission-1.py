class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        indices = []
        for n in range(len(nums)):
            complement = target - nums[n]
            if complement in h:
                indices.extend([h[complement], n])
            h[nums[n]] = n
        return indices