
class Solution:
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        c=0
        dt={}
        mm=10 ** 9 + 7
        for i in range(len(A)):
            temp=1
            j=0
            while A[j]*A[j]<A[i]:
                if A[i]%A[j]==0 and A[i]//A[j] in dt:
                    temp+=dt[A[j]]*dt[A[i]//A[j]]*2
                j+=1
            if A[j]*A[j]==A[i]:
                temp+=dt[A[j]]*dt[A[j]]
            temp%=mm
            dt[A[i]]=temp
            c+=temp
        return c%mm

print(Solution().numFactoredBinaryTrees([2, 4, 5, 10]))