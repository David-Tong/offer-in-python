class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def swap(x, y):
            nums[x], nums[y] = nums[y], nums[x]

        L = len(nums)

        idx = 0
        idx2 = 0

        while idx < L:
            if nums[idx] % 2 == 1:
                if idx != idx2:
                    swap(idx, idx2)
                idx2 += 1
            idx += 1

        return nums


nums = [1,2,3,4]
nums = [1,2,4,8,12,5,7,9]
nums = []

solution = Solution()
print(solution.exchange(nums))
