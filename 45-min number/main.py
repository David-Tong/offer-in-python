class Solution(object):
    def minNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(_) for _ in nums]

        def compare(num, num2):
            if int(num + num2) <= int(num2 + num):
                return -1
            else:
                return 1

        def swap(x, y):
            nums[x], nums[y] = nums[y], nums[x]

        L = len(nums)
        for x in range(L):
            mini = x
            for y in range(x + 1, L):
                if compare(nums[mini], nums[y]) > 0:
                    mini = y
            if mini != x:
                swap(x, mini)
        return "".join(nums)


nums = [10, 2]
nums = [3,30,34,5,9]
nums = [2,20,21,22,23,3,34,31,35,203,301]


solution = Solution()
print(solution.minNumber(nums))
