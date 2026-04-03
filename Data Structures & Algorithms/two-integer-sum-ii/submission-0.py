class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # define left and right pointers
        left = 0
        right = len(numbers) -1

        while left < right:
            # Answer found
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]

            # Decrement right pointer if sum is greater than target
            if numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left +=1
        return [0,0]