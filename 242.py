class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        items = {}
        for i in s:
            if i not in items:
                items[i] = 1
            else:
                items[i] += 1
        items2 = {}
        for i in t:
            if i not in items2:
                items2[i] = 1
            else:
                items2[i] += 1
        if items == items2:
            return True
        return False
