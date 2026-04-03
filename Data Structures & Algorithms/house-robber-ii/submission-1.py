class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self.helper(nums[1:]), self.helper(nums[:-1])) # Skip first house and last house 

    def helper(self, nums):
        rob1 = 0
        rob2 = 0

        for i in nums:
            newRob = max(i + rob1, rob2) # i is adjacent to rob2
            rob1 = rob2
            rob2 = newRob
        return rob2
