class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        while(len(nums1) > m):
            nums1.remove(nums1[m])
        while(len(nums2) > n):
            nums1.remove(nums1[n])
        nums1.extend(nums2)
        nums1.sort()

            