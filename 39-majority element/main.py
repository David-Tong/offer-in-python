class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        number = nums[0]
        count = 1
        for num in nums[1:]:
            if count > 0:
                if num == number:
                    count += 1
                else:
                    count -= 1
            elif count == 0:
                number = num
                count += 1
        return number


nums = [1, 2, 3, 2, 2, 2, 5, 4, 2]
nums = [2, 2, 2, 3, 4, 3]
nums = [2, 2, 2, 3, 4, 5]

solution = Solution()
print(solution.majorityElement(nums))
