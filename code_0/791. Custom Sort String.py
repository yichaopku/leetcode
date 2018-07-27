class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        dt={}
        for i in range(len(S)):
            dt[S[i]]=i
        s=len(dt)
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if c not in dt:
                dt[c]=s
                s+=1
        dt1={dt[k]:k for k in dt}
        ref=[0]*26
        for c in T:
            ref[dt[c]]+=1
        rs=''
        for i in range(len(ref)):
            rs+=dt1[i]*ref[i]
        return rs

print(Solution().customSortString(S = "cba",
T = "abcd"))