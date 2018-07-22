class Solution:
    def recursive(self,integers,total):
        if integers in self.cache:
            return self.cache[integers]

        for i in range(self.mm-1,-1,-1):
            if not (integers>>i)&1:
                if i+1>=total or self.recursive(integers|(1<<i),total-i-1)==False:
                    self.cache[integers]=True
                    return True
        self.cache[integers] = False
        return False

    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        ss=maxChoosableInteger*(maxChoosableInteger+1)//2
        if ss<desiredTotal:
            return False
        if ss==desiredTotal:
            return True if maxChoosableInteger%2==1 else False
        self.cache={}
        self.mm=maxChoosableInteger
        return self.recursive(0,desiredTotal)

print(Solution().canIWin(10,20))