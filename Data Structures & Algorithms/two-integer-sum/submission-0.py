class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        for i in range(size):
            for j in range(i,size):
                if (nums[i] + nums[j]) == target and i != j: 
                    return [i,j]
                
        