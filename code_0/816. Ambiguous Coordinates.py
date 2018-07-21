class Solution:
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        rs=[]
        S=S[1:-1]
        for i in range(1,len(S)):
            b,e=S[:i],S[i:]
            for j in range(1,len(b)+1):
                bb,be=b[:j],b[j:]
                if be=='':
                    if str(int(bb))==bb:
                        temp=bb
                    else:
                        continue
                else:
                    if be[-1]=='0':
                        continue
                    if str(int(bb))!=bb:
                        continue
                    temp=bb+'.'+be
                for k in range(1,len(e)+1):
                    eb, ee = e[:k], e[k:]
                    if ee == '':
                        if str(int(eb)) == eb:
                            temp1 = eb
                            rs.append('('+temp+', '+temp1+')')
                    else:
                        if ee[-1] == '0':
                            continue
                        if str(int(eb))!=eb:
                            continue
                        temp1 = eb + '.' + ee
                        rs.append('(' + temp + ', ' + temp1 + ')')
        return rs

print(Solution().ambiguousCoordinates("(100)"))