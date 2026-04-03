class Solution:
    def climbStairs(self, n: int) -> int:
        # 2 pointers representing the num of steps we take to reach prev step
        one = 1 
        two = 1 

        for i in range(n - 1): 
            temp = one
            one = one + two
            two = temp # Shift variables forwards

        return one
