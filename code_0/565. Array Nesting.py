class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dt={}
        ll=0
        for n in nums:
            if n in dt:
                continue
            temp={}
            val=n
            while val not in temp:
                temp[val]=-1
                dt[val]=-1
                val=nums[val]
            ll=ll if ll>len(temp) else len(temp)
        return ll

print(Solution().arrayNesting([5,4,0,3,1,6,2]))