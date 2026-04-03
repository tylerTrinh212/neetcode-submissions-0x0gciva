class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         array = []
         size = len(nums)
         for i in nums:
            if(i not in array):
                array.append(i)
            else:
                return True
         return False
