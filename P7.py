class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x > 0:
            val = int(str(x)[::-1])
        else:
            val = -1*int(str(x*-1)[::-1])

        if val < -2**31 or val > 2**31 - 1:
            return 0
        else:
            return val