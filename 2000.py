class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        x = word.find(ch)
        copy = (word[:x+1])[::-1]
        return copy + word[x+1:]
        