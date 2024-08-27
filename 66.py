class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits)-1
        j = 0
        summ = 0
        while i > -1:
            exponent = 10 ** j
            summ =  summ + (exponent * digits[i])
            i -= 1
            j += 1
        summ += 1
        return [int(x) for x in str(summ)]