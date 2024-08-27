class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        count = 0
        for i in sentences:
            temp = i.count(" ") + 1
            if temp > count:
                count = temp
        return count

        