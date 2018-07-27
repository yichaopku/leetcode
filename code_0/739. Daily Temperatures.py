class Solution:

    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack=[[temperatures[-1],len(temperatures)-1]]
        rs=[0]
        for i in range(len(temperatures)-2,-1,-1):
            if temperatures[i]<stack[-1][0]:
                rs.append(1)
                stack.append([temperatures[i],i])
            else:
                while stack and stack[-1][0]<=temperatures[i]:
                    stack.pop()
                if stack:
                    rs.append(stack[-1][1]-i)
                else:
                    rs.append(0)
                stack.append([temperatures[i],i])
        rs.reverse()
        return rs

print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))