def BFSListLevelPath(AList,start,preventionList):
  visited,parent={},{}
  for i in range(len(AList)):
    visited[i]=False
    parent[i]=-1

  q=[]
  visited[start]=True
  q.append(start)

  while len(q)>0:
    j=q.pop(0)
    for k in AList[j]:
      if not visited[k] and not k in preventionList:
        visited[k]=True
        parent[k]=j
        q.append(k)

  return (visited,parent)

def findpath(parent,start,end):
  L=[]
  curr=parent[end]
  while curr!=start:
    L.append(curr)
    curr=parent[curr]

  return L

def backandforth(AList, end1, end2):
  preventionList = []
  c = 0
  visited, parent = BFSListLevelPath(AList, end1,preventionList)
  while visited[end2]:
      c += 1
      path = findpath(parent, end1, end2)
      preventionList.extend(path)
      visited, parent = BFSListLevelPath(AList, end1, preventionList)
  return c