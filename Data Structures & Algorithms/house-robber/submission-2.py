class Solution:
    def rob(self, nums: List[int]) -> int:
        map = [-1] * len(nums) # Store past recursion results

        def dfs(i):
            # Base case
            if i >= len(nums):
                return 0
            if map[i] != -1:
                return map[i]
            
            map[i] = max(nums[i] + dfs(i+2), dfs(i+1))
            return map[i]

        return dfs(0)
