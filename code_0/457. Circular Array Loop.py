class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)):
            if nums!=[0]:
                index0,index1,index11=i,i,i
                neg=None
                while True:
                    index1 = (index1 + nums[index1]) % len(nums)
                    index11 = (index11 + nums[index11]) % len(nums)
                    if nums[index11]*nums[index0]<=0:
                        neg=index11
                        break
                    index11 = (index11 + nums[index11]) % len(nums)
                    if nums[index11] * nums[index0] <= 0:
                        neg = index11
                        break
                    if index1==index11:
                        break
                if neg:
                    while index0 != neg:
                        temp = nums[index0]
                        nums[index0] = 0
                        index0 = (index0 + temp) % len(nums)
                else:
                    index11 = (index11 + nums[index11]) % len(nums)
                    if index1!=index11:
                        return True
                    while True:
                        temp=nums[index0]
                        nums[index0]=0
                        index0 = (index0 + temp) % len(nums)
                        if nums[index0]==0:
                            break
        return False

print(Solution().circularArrayLoop( [-1,
-2,
-3,
-4,
-5]))