class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        from bisect import bisect_left, bisect_right
        idx_left = bisect_left(nums, target)
        idx_right = bisect_right(nums, target)

        return idx_right - idx_left


nums = [5,7,7,8,8,10]
target = 8
target = 6

solution = Solution()
print(solution.search(nums, target))
