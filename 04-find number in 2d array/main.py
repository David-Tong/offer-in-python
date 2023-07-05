class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        M = len(matrix)
        if M == 0:
            return False
        N = len(matrix[0])
        if N == 0:
            return False

        # find row
        left = 0
        right = M - 1

        while left + 1 < right:
            middle = (left + right) // 2
            if matrix[middle][0] > target:
                right = middle - 1
            else:
                left = middle

        if matrix[left][0] > target:
            return False
        elif matrix[right][0] > target:
            row = left
        else:
            row = right

        # search column
        idx = 0
        while idx <= row:
            left = 0
            right = N - 1

            while left + 1 < right:
                middle = (left + right) // 2
                if matrix[idx][middle] > target:
                    right = middle - 1
                else:
                    left = middle

            if matrix[idx][left] == target or matrix[idx][right] == target:
                return True
            idx += 1
        return False


matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 5
target = 20
target = 0
target = 22
target = 31

matrix = [[1,2,5,6,7]]
matrix = [1,2,5,6,7]
target = 5
target = 4

matrix = [[]]

solution = Solution()
print(solution.findNumberIn2DArray(matrix, target))