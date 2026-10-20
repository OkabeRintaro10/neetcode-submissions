class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        num_set = set(nums)
        ls = 0
        for num in num_set:
            if num - 1 not in num_set:
                curr = num
                curr_streak = 1
                while curr + 1 in num_set:
                    curr += 1
                    curr_streak += 1
                ls = max(ls, curr_streak)
        return ls
