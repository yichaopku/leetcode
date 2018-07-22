class Solution:
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        dt={position[i]:speed[i] for i in range(len(position))}
        position.sort(reverse=True)
        position=[(target-i)/dt[i] for i in position]
        index0=0
        index1=1
        c=0
        while index0<len(position):
            while index1<len(position) and position[index0]>=position[index1]:
                index1+=1
            c+=1
            index0=index1
            index1+=1
        return c

print(Solution().carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]))
