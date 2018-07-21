class Solution:
    def recursive(self,k,res):
        if k==self.target:
            self.rs.append(res+[k])
            return
        for i in self.graph[k]:
            self.recursive(i,res+[k])

    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.rs=[]
        self.target=len(graph)-1
        self.graph=graph
        self.recursive(0,[])
        return self.rs

print(Solution().allPathsSourceTarget([[1,2], [3], [3], []] ))