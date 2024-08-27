class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        l1 = list(word1)
        l2 = list(word2)
        i = 0
        index = 1
        while i < len(word2):
            l1.insert(index, l2[i])
            index += 2
            i += 1
        return''.join(l1)

        