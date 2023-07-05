class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        L = len(nums)

        left = 0
        right = L - 1

        while left < right:
            total = nums[left] + nums[right]
            if total == target:
                return [nums[left], nums[right]]
            elif total < target:
                left += 1
            else:
                right -= 1


nums = [2,7,11,15]
target = 9

nums = [10,26,30,31,47,60]
target = 40

solution = Solution()
print(solution.twoSum(nums, target))
