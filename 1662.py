class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        if "".join(tuple(word1)) ==  "".join(tuple(word2)):
            return True
        return False