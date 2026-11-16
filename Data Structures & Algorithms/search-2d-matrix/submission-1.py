class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix)-1
        n = len(matrix[0])-1
        while start <= end:
            mid = (start + end)//2
            if target < matrix[mid][0]:
                end = mid -1
            elif target > matrix[mid][n]:
                start = mid + 1
            else:
                break
        
        if not (start <= end):
            return False
        
        row = (start + end) // 2
        left, right = 0, n
        while left <= right:
            mid = (left+right) // 2
            if target > matrix[row][mid]:
                left = mid+1
            elif target < matrix[row][mid]:
                right = mid-1
            else:
                return True
        
        return False 