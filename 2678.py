class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """ 
        j = 0
        for i in details:
            if int(i[-4:-2]) > 60:
                j += 1
        return j