class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        lCount = 0
        rCount = 0
        j = len(nums) -1
        while i < len(nums):
            lCount += nums[i]
            i += 1
            rCount += nums[j]
            j -= 1
            if(lCount == rCount):
                return i
            else:
                return -1   