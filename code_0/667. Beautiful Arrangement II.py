class Solution:

    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        if n==1:
            return [1]
        if k==1:
            return list(range(1,n+1))
        head=list(range(1,n-k+1))
        index1=n-k+1
        index2=n
        while index1<index2:
            head.append(index2)
            head.append(index1)
            index2-=1
            index1+=1
        if index1==index2:
            head.append(index2)
        return head

print(Solution().constructArray(10,3))