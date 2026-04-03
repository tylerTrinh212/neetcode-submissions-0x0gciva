class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) -1
        answer = nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                answer = min(answer, nums[left])
                break

            mid = (left + right) // 2
            answer = min(answer, nums[mid])
            if nums[mid] >= nums[left]: # We are in left sorted, so check right sorted, 
                                        # we can assume that right side is always less than due to rotating
                left = mid + 1
            else: # We are in right side so look left for anything smaller
                right = mid -1
        return answer