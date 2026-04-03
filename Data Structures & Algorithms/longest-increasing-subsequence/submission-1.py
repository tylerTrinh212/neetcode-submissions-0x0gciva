class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1): #iterate backwards
            for j in range(i + 1, len(nums)): # Check every entry after i
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
                    # Get LIS of either num i by itself or the increaseing subsequence from the if statement
        
        return max(LIS)