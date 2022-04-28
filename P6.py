class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if (numRows == 1):
            return s
        
        down = True
        res = ["" for x in range(len(s))]
        row = 0
        for i in range(len(s)):
            res[row] += s[i]

            if row == numRows-1:
                down = False
            elif row == 0:
                down = True

            if down:
                row += 1
            else:
                row -= 1

        return "".join(res)
