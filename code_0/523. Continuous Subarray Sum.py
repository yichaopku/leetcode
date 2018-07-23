class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums)<=1:
            return False
        for i in range(len(nums) - 1):
            if nums[i] == 0 and nums[i + 1] == 0:
                return True
        if k==0:
            return False
        k=k if k>0 else -k
        dt={}
        ss=0
        for i in range(len(nums)):
            ss+=nums[i]
            ss%=k
            if (ss==0 and i!=0) or (ss in dt and i-dt[ss]>1):
                return True
            if ss not in dt:
                dt[ss]=i
        return False

print(Solution().checkSubarraySum([5,2,4],  k=5))