L=[]
fd=open("Coord.txt","r")
count=fd.readline()
for i in range(int(count)):
    x,y=fd.readline().split()
    L.append([int(x),int(y)])

L=sorted(L,key=lambda x:(x[0],x[1]))

for i in L:
    print(*i)

fd.close()