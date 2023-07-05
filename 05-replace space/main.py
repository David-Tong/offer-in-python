class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        L = len(s)

        idx = 0
        ans = ""
        while idx < L:
            if s[idx] == " ":
                ans += "%20"
            else:
                ans += s[idx]
            idx += 1
        return ans


s = "We are happy."
s = "We are  happy."

solution = Solution()
print(solution.replaceSpace(s))
