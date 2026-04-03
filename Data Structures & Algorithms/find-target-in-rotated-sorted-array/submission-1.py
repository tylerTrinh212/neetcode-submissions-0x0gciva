class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1

        
        while left <= right:

            mid = (left + right) // 2
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[mid] >= nums[left]:
                # If target is greater than mid less than left, check right half
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            # right sorted portion
            else:
                # If target is greater than right or is less than mid, check left half
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
            
        return -1

