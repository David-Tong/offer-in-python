class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import defaultdict
        dicts = defaultdict(int)
        queue = list()
        for ch in s:
            if dicts[ch] == 0:
                queue.append(ch)
            dicts[ch] += 1

        ans = " "
        for ch in queue:
            if dicts[ch] == 1:
                ans = ch
                break
        return ans


s = "abaccdeff"
s = "abbccddeea"
s = ""

solution = Solution()
print(solution.firstUniqChar(s))
