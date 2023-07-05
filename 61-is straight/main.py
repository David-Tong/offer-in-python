class Solution(object):
    def isStraight(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        L = len(nums)
        nums = sorted(nums)

        wildcard = 0
        for x in range(L):
            if nums[x] == 0:
                wildcard += 1

        for x in range(wildcard, L - 1):
            if nums[x] == nums[x + 1]:
                return False
            wildcard -= nums[x + 1] - nums[x] - 1
            if wildcard < 0:
                return False
        return True


nums = [1,2,3,4,5]
nums = [0,0,1,2,5]
nums = [1,2,4,5,6]
nums = [0,0,0,0,0]
nums = [0,0,2,2,5]

solution = Solution()
print(solution.isStraight(nums))
