class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]

        minProduct = nums[0]
        maxProduct = nums[0]
        
        for i in range(1, len(nums)):
            oldMax = maxProduct
            oldMin = minProduct
            
            maxProduct = max(oldMax * nums[i], oldMin * nums[i], nums[i])
            minProduct = min(oldMax * nums[i], oldMin * nums[i], nums[i])

            result = max(result, maxProduct)
        
        return result
