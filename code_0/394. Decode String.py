class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ''
        index = 0
        stack = []
        while index < len(s):
            if s[index].isdigit():
                temp = index + 1
                while temp < len(s) and s[temp].isdigit():
                    temp += 1
                stack.append(int(s[index:temp]))
                index = temp
            elif s[index] == '[':
                index += 1
                continue
            elif s[index] == ']':
                index += 1
                if stack:
                    rep_s = stack.pop()
                    rep_t = stack.pop()
                    stack.append(rep_s*rep_t)
                while len(stack) > 1:
                    if not isinstance(stack[-2], int):
                        tail = stack.pop()
                        stack[-1] += tail
                    else:
                        break
            else:
                temp = index + 1
                while temp < len(s) and s[temp].isalpha():
                    temp += 1
                stack.append(s[index:temp])
                while len(stack) > 1:
                    if not isinstance(stack[-2], int):
                        tail = stack.pop()
                        stack[-1] += tail
                    else:
                        break
                index = temp
        return stack[-1]


print(Solution().decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))
