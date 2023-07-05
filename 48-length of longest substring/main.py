class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        L = len(s)

        def duplicate():
            for key in dicts:
                if dicts[key] > 1:
                    return True
            return False

        from collections import defaultdict
        dicts = defaultdict(int)

        left = 0
        right = 0

        ans = 0
        while right < L:
            dicts[s[right]] += 1

            while duplicate():
                dicts[s[left]] -= 1
                if dicts[s[left]] == 0:
                    del dicts[s[left]]
                left += 1

            ans = max(ans, right - left + 1)
            right += 1
        return ans


s = "abcabcbb"
s = "bbbbb"
s = "pwwkew"
s = ""

solution = Solution()
print(solution.lengthOfLongestSubstring(s))


