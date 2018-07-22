class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        dt={}
        for i in range(len(wall)):
            c=0
            for j in range(len(wall[i])-1):
                c+=wall[i][j]
                if c in dt:
                    dt[c]+=1
                else:
                    dt[c]=1
        if len(dt)==0:
            return len(wall)
        return len(wall)-max(dt.values())

print(Solution().leastBricks([[1,2,2,1],
 [3,1,2],
 [1,3,2],
 [2,4],
 [3,1,2],
 [1,3,1,1]]))