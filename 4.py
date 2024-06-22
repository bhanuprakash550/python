l=list(map(int,input("enter").split(",")))
n=len(l)
a=set(l)
n1=len(a)
l=list(a)
for i in range(n1,n):
    l.append('_')
print(n1,l)
        
