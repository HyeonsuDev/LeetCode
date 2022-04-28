class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        r = nums1 + nums2
        r.sort()
        l = len(r)

        mid = l / 2
        
        if l % 2 == 0:
            return float(r[mid] + r[mid - 1]) / 2
        else:
            return r[mid]