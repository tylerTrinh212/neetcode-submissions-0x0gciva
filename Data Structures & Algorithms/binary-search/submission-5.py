class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2 # Get middle index
            # Look at left half of array
            if target < nums[mid]:
                right = mid - 1
            # Look at right half
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        return -1
