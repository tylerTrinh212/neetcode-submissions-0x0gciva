class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        # Use binary search per row to find target
        # If target is not within the left and right bounds of middle row, move up if less than or down if not

        # Pointers to determine middle row
        leftRow = 0
        rightRow = rows - 1

        # Find row that may contain target
        while leftRow <= rightRow:
            midRow = (leftRow + rightRow) // 2
            if target < matrix[midRow][0]:
                rightRow = midRow - 1
            elif target > matrix[midRow][-1]:
                leftRow = midRow + 1
            else: 
                break
        
        # Pointers for binary search within row that may contain target
        left = 0
        right = columns - 1


        if not (leftRow <= rightRow):
            return False

        while left <= right:
            mid = (left + right) // 2

            if matrix[midRow][mid] == target:
                return True

            elif target > matrix[midRow][mid]:
                left = mid + 1

            elif target < matrix[midRow][mid]:
                right = mid - 1


        return False