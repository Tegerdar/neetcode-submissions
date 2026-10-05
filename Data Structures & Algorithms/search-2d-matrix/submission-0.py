class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                return self.findNumber(matrix[mid], target)
            elif target >= matrix[mid][-1]:
                left = mid + 1
            else:
                right = mid - 1
        return False
        
    def findNumber(self, row: List[int], target: int) -> bool:
        left, right = 0, len(row) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target == row[mid]:
                return True
            elif target < row[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False