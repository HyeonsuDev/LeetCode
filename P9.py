from operator import truediv


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        s = str(x)
        if s[0] == '-':
            return False
        
        n = len(s)

        left, right = 0, n - 1

        while left < n and right >= 0 and left < right and s[left] == s[right]:
            left += 1
            right -= 1

        if left == right or left > right:
            return True
        else:
            return False