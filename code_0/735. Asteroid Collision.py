class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack=[]
        index=0
        while index<len(asteroids) and asteroids[index]<0:
            stack.append(asteroids[index])
            index+=1
        while index<len(asteroids) and asteroids[index]>0:
            stack.append(asteroids[index])
            index+=1
        while index<len(asteroids):
            if asteroids[index]>0:
                stack.append(asteroids[index])
            else:
                while True:
                    if not stack:
                        stack.append(asteroids[index])
                        break
                    else:
                        if stack[-1]>0:
                            if stack[-1]+asteroids[index]==0:
                                stack.pop()
                                break
                            elif stack[-1]+asteroids[index]<0:
                                stack.pop()
                            else:
                                break
                        else:
                            stack.append(asteroids[index])
                            break
            index+=1
        return stack

print(Solution().asteroidCollision([-2, -1, 1, 2]))