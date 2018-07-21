class Solution:

    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack=[]
        s=None
        for n in nums[::-1]:
            if s and n<s:
                return True
            while stack and n>stack[-1]:
                s=stack.pop()
            stack.append(n)
        return False

print(Solution().find132pattern([-1,3,2,0]))