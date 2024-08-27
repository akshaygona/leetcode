class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        countWords = 0
        for i in words1:
            if words1.count(i) == words2.count(i) == 1:
                countWords += 1
        return countWords
                