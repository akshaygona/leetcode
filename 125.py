import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(r'[^a-zA-Z0-9\s]', '', s)
        s = s.lower()
        s = s.replace(" ","")
        if s == s[::-1]:
            return True
        else:
            return False