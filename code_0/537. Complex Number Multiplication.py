class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        x1,y1=a[:-1].split('+')
        x2,y2=b[:-1].split('+')
        x1,y1,x2,y2=int(x1),int(y1),int(x2),int(y2)
        c=x1*x2-y1*y2
        d=x1*y2+x2*y1
        return str(c)+'+'+str(d)+'i'

print(Solution().complexNumberMultiply("1+-1i", "1+-1i"))