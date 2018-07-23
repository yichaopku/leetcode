import heapq
class Solution:

    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        queue=[[0,src,-1]]
        dt={}
        for b,e,v in flights:
            if b in dt:
                dt[b].append([e,v])
            else:
                dt[b]=[[e,v]]
        while queue:
            item=heapq.heappop(queue)
            if item[1]==dst:
                return item[0]
            if item[2]==K:
                continue
            if item[1] in dt:
                for i in dt[item[1]]:
                    heapq.heappush(queue,[i[1]+item[0],i[0],1+item[2]])

        return -1

print(Solution().findCheapestPrice(5,
[[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]],
2,
1,
1))

