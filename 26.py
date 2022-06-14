N,P=map(int,input().split())

L=[i for i in range(2,N+1)]
LL=[]
for i in range(2,L[-1]+1):
    for j in range(2,i+1):
        if i==j:
            LL.append(i)
        if i%j==0:
            break

for i in range(len(LL)):
    k=LL[i]
    for j in range(N):
        if k>L[-1]:
            break
        if k in L:
            if P==1:
                print(k)
                exit()
            L.remove(k)
            P-=1
        k=LL[i]*(j+2)
