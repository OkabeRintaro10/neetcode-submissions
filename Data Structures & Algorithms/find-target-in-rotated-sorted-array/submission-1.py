class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_idx, right_idx = 0, len(nums) - 1

        while left_idx <= right_idx:
            mid = (left_idx + right_idx) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left_idx] <= nums[mid]:

                if nums[left_idx] <= target < nums[mid]:
                    right_idx = mid - 1
                else:
                    left_idx = mid + 1

            # Right half is sorted
            else:

                if nums[mid] < target <= nums[right_idx]:
                    left_idx = mid + 1
                else:
                    right_idx = mid - 1

        return -1