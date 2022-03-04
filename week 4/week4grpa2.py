def findMasterTank(tanks,pipes):
    indegree={}
    for i in tanks:
        indegree[i]=0
    for j in range(len(pipes)):
        indegree[pipes[j][1]]+=1
    mastertanks=[]
    for j in indegree.keys():
        if(indegree[j]==0):
            mastertanks.append(j)
    if(len(mastertanks)==1):
        return (mastertanks[0])
    else:
        return 0
        
v = [item for item in input().split(" ")]
#Tanks(vertices) numbered from 1 to n in string format.
numberOfEdges = int(input())
e = []
for i in range(numberOfEdges):
  s = input().split(" ")
  e.append((s[0], s[1]))
print(findMasterTank(v, e))