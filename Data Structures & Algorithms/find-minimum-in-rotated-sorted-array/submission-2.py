class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        answer = nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                answer = min(nums[left], answer)
                break

            mid = (left + right) // 2
            answer = min(answer, nums[mid])

            if nums[mid] >= nums[left]: 
                left = mid + 1
            else:
                right = mid - 1

        return answer