def findConnectionLevel(n,Gmat,Px,Py):
    a_l={}
    for i in range(n):
        a_l[i]=[]
        for j in range(n):
            if Gmat[i][j]==1:
                a_l[i].append(j)
    
    level={}
    for i in range(n):
        level[i]=-1
    
    l=[]
    l.append(Px)
    level[Px]=0
    
    while (l):
        a=l[0]
        l=l[1:]
        for i in a_l[a]:
            if level[i]==-1:
                level[i] =level[a]+1
                l.append(i)
    
    if level[Py]==-1:
        return(0)
    return(level[Py])
vertices = int(input())
Amat = []
for i in range(vertices):
  row = [int(item) for item in input().split(" ")]
  Amat.append(row)
personX = int(input())
personY = int(input())
print(findConnectionLevel(vertices, Amat, personX, personY))