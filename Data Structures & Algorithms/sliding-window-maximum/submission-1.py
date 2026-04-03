class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque() # indexes
        l = 0
        r = 0

        while r < len(nums):
            # pop smaller values from q when q is non empty and new num is greater than last one in queue
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left val from window
            if l > q[0]:
                q.popleft()
            
            # Only move left pointer when window size is k
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output
