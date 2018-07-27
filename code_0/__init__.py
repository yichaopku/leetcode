# test

def f1(p):
    c=0
    for i in range(1,p+1):
        if p%i==0:
            c+=1
    return c

def f2(p):
    c=1
    i=2
    while i*i<=p:
        temp=0
        while p%i==0:
            temp+=1
            p//=i
        c*=(temp+1)
        i+=1
    return c*2 if p>1 else c

for i in range(1,10000):
    # print(i)
    if f1(i)!=f2(i):
        print(i)
