
class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        N0=N
        alpha=1
        while N0%2==0:
            alpha+=1
            N0//=2

        c=1
        i=3
        while i*i<=N0:
            temp=0
            while N0%i==0:
                temp+=1
                N0//=i
            i+=2
            c*=(temp+1)
        return c*2 if N0>1 else c

print(Solution().consecutiveNumbersSum(225))