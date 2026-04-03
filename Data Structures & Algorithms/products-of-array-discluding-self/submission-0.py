class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i == j:
                    continue # Don't multiply the same number twice
                else:
                    answer[i] = answer[i] * nums[j]
        return answer