class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        
        while left <= right:
            # Get middle index
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # Look at left half
            elif nums[mid] < target:
                left = mid +1

            # Look at right half
            elif nums[mid] > target:
                right = mid -1
        return -1
        