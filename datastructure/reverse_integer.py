#conding=utf-8
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #需要判断逆置数字的正负，正：大于2^31-1，负：小于-2^31
        if x > 0:
        	x = int(str(x)[::-1])
        else:
        	x = - int(str(-x)[::-1])

        if x <= 2147483647 and x >= -2147483648:
        	return x
        else:
        	return 0

        
