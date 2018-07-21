class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        operator={'+','-','*','/'}
        spt=[]
        index=0
        has_operator=False
        for i in range(len(s)):
           if s[i] in operator:
               has_operator=True
               spt.append(int(s[index:i]))
               spt.append(s[i])
               index=i+1
        if not has_operator:
            return int(s)
        spt.append(int(s[index:]))

        oo = []
        nn = []
        for v in spt:
            if v in operator:
                oo.append(v)
            else:
                nn.append(v)
                if len(oo)==0:
                    continue
                else:
                    pornot=False
                    if oo[-1]=='*':
                        e=nn.pop()
                        b=nn.pop()
                        nn.append(b*e)
                        pornot=True
                    elif oo[-1]=='/':
                        e = nn.pop()
                        b = nn.pop()
                        nn.append(b // e)
                        pornot = True
                    if pornot:
                        oo.pop()
        sss=nn[0]
        index=1
        for c in oo:
            if c=='+':
                sss+=nn[index]
            else:
                sss-=nn[index]
            index+=1
        return sss

print(Solution().calculate("2*3+4"))





