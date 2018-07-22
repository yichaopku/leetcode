class Solution:

    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """

        def recursive(n, ps):
            if n == 1:
                return 1
            temp = (n, ps)
            if temp in cache:
                return cache[temp]
            s = 0
            for i in range(len(ps)):
                if ps[i] % n == 0 or n % ps[i] == 0:
                    s += recursive(n - 1, ps[:i] + ps[i + 1:])
            cache[temp] = s
            return s

        cache={}
        return recursive(N,tuple(range(1,N+1)))

print(Solution().countArrangement(2))