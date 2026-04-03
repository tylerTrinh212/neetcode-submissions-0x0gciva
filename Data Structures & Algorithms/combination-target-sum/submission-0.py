class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []

        def dfs(i, currentList, total):
            # Base case: found list with sum equal to target
            if total == target:
                result.append(currentList.copy())
                return
            # Base case: If we go over target or run out of options
            if i >= len(nums) or total > target:
                return

            currentList.append(nums[i])
            # Left tree includes i index
            dfs(i, currentList, total + nums[i])
            currentList.pop()
            # Right tree doesn't include current num[i] to ensure lists have unique values
            dfs(i + 1, currentList, total)
        
        dfs(0, [], 0)
        return result
