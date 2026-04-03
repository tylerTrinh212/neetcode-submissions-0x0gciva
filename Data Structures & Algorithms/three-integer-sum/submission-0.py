class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, a in enumerate(nums):
            # Check for duplicate first number
            if i > 0 and a == nums[i-1]:
                continue
            # Set left and right pointers
            left = i+1
            right = len(nums) -1

            while left < right:
                threeSum = a + nums[left] + nums[right]
                # If too small, shift right pointer to left
                if threeSum > 0:
                    right -= 1
                # If too large, shift left pointer to right
                elif threeSum < 0:
                    left +=1
                # Else we append solution
                else:
                    result.append([a, nums[left], nums[right]])
                    left +=1
                    # After getting one solution, shift left pointer until we find new value
                    while nums[left] == nums[left-1] and left < right:
                        left +=1
        return result
    