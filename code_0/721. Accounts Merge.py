class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        accs={}
        for a in accounts:
            if a[0] not in accs:
                accs[a[0]]=[set(a[1:])]
            else:
                temp=set(a[1:])
                lst=accs[a[0]]
                ok=[]
                for s in range(len(lst)):
                    if lst[s].intersection(temp):
                        ok.append(s)
                if not ok:
                    accs[a[0]].append(temp)
                else:
                    for i in range(len(ok)-1,0,-1):
                        lst[ok[0]].update(lst[ok[i]])
                        lst.pop(ok[i])
                    lst[ok[0]].update(temp)
        rs=[]
        for name in accs:
            for s in accs[name]:
                temp=list(s)
                temp.sort()
                rs.append([name]+temp)
        return rs

print(Solution().accountsMerge(accounts =[["David","David0@m.co","David1@m.co","David2@m.co"],["David","David2@m.co","David3@m.co","David4@m.co","David5@m.co"]]))
