class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = nums[0]
        for i in range(1,len(nums)):
            # If it's better to use same subarray instead of starting new one
            if currSum + nums[i] > nums[i]:
                currSum += nums[i]
            else:
                currSum = nums[i]
            # Update maximum subarray
            if currSum > maxSum:
                maxSum = currSum
        return maxSum
                
            