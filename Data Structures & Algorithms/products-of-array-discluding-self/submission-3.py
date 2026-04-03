class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        prefix = 1
        # Store prefixes from left to right in result
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i] # Prefix will be all products before i

        postfix = 1
        # Store postfixes from right to left in result   
        for i in range(len(nums) -1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i] # Postfix will be all products after i

        return result 