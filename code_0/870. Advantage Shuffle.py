class Solution:
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        A.sort(reverse=True)
        b=B[:]
        b.sort(reverse=True)
        rs=[]
        mp={}
        index=0
        for n in range(len(A)):
            while index<len(B) and A[n]<=b[index]:
                index+=1
            if index==len(B):
                break
            else:
                if b[index] in mp:
                    mp[b[index]].append(A[n])
                else:
                    mp[b[index]]=[A[n]]
                index+=1
        for i in B:
            if i in mp and len(mp[i])>0:
                rs.append(mp[i].pop())
            else:
                rs.append(A[n])
                n+=1
        return rs

print(Solution().advantageCount([2,0,4,1,2],[1,3,0,0,2]))