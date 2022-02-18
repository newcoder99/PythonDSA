def DFSInit(AMat):
  (rows,cols)=(AMat.shape)
  (visited,parent)=({},{})
  for i in range(rows):
    visited[i]=False
    parent[i]=-1

  return (visited,parent)

def neighbours(AMat,i):
    nbrs=[]
    (rows,cols)=(AMat.shape)
    for j in range(cols):
      if AMat[i,j]==1:
        nbrs.append(j)
    return nbrs


def DFS(AMat,visited,parent,v):
  visited[v]=True

  for k in neighbours(AMat,v):
    if not visited[v]:
      parent[k]=v
      (visited,parent)=DFS(AMat,visited,parent,v)
  
  return (visited,parent)


def DFSInitList(AList):
  (visited,parent)=({},{})

  for i in  AList.keys():
    visited[i]=False
    parent[i]=-1

  return (visited,parent)

def DFSList(AList,visited,parent,v):
  visited[v]=True

  for k in AList[v]:
    if not visited[k]:
      parent[k]=v
      (visited,parent)=DFSList(AList,visited,parent,v)
  
  return (visited,parent)