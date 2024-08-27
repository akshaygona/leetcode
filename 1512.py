class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(0,len(nums)):
            j = i + 1
            while j < len(nums):
                if nums[i] == nums[j]:
                    count += 1
                j += 1
        return count