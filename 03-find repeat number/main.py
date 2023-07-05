class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [x + 1 for x in nums]

        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] *= -1
            elif nums[idx] < 0:
                return idx
        return 0


nums = [2, 3, 1, 0, 2, 5, 3]
nums = [0, 0, 1, 2, 3, 4]
nums = [1, 1, 1]
nums = [3, 4, 2, 1, 1, 0]
nums = [1, 0, 1, 4, 2, 5, 3]

solution = Solution()
print(solution.findRepeatNumber(nums))
