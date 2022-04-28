class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        resLen = 0
        for i in range(len(s)):
            res = max(res, expand(i, i), expand(i, i + 1), key=len)
        
        def expand(self, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left:right + 1]

        return res
