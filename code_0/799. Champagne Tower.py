class Solution:
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        if poured==0:
            return 0
        if query_row==0:
            return poured if poured<1 else 1
        first=[poured]
        for i in range(query_row-1):
            temp=[0 for i in range(len(first)+1)]
            temp[0]=(first[0]-1)/2 if first[0]>1 else 0
            temp[-1]=temp[0]
            for j in range(1,(len(temp)+1)//2):
                temp[j]=((first[j-1]-1)/2 if first[j-1]>1 else 0)+((first[j]-1)/2 if first[j]>1 else 0)
                temp[-j-1]=temp[j]
            first=temp
        if query_glass==0 or query_glass==len(first):
            temp= (first[0]-1)/2 if first[0]>1 else 0
            return temp if temp<=1 else 1
        temp= ((first[query_glass-1]-1)/2 if first[query_glass-1]>1 else 0)+((first[query_glass]-1)/2 if first[query_glass]>1 else 0)
        return temp if temp <= 1 else 1

print(Solution().champagneTower(4,
1,
0))