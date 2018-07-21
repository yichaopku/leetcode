class Solution:
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        for i  in range(1,len(num)-1):
            for j in range(i+1,len(num)):
                s,e=num[:i],num[i:j]
                if (s[0]=='0' and len(s)>1) or (e[0]=='0' and len(e)>1):
                    continue
                index=j
                while index<=len(num):
                    temp=str(int(s)+int(e))
                    if not num.startswith(temp,index):
                        break
                    else:
                        index+=len(temp)
                        s,e=e,temp
                    if index==len(num):
                        return True
        return False

print(Solution().isAdditiveNumber("123"))