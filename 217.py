class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        items = {}
        for i in nums:
            if i not in items:
                items[i] = 1
            else: 
                items[i] += 1
        for i in items:
            if items.get(i) > 1:
                return True
        return False