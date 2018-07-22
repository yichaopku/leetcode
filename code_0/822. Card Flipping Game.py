
class Solution:
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        dt={}
        for i in range(len(fronts)):
            if fronts[i]==backs[i]:
                dt[fronts[i]]=-1
        c=3000
        for i in range(len(backs)):
            if fronts[i] not in dt:
                c=fronts[i] if c>fronts[i] else c
            if backs[i] not in dt:
                c=backs[i] if c>backs[i] else c
        return 0 if c==3000 else c

print(Solution().flipgame(fronts = [1,2,4,4,7], backs = [1,3,4,1,3]))