def BFSListLevelPath(AList,v):
  level,parent={},{}
  for i in range(len(AList)):
    level[i]=-1
    parent[i]=-1

  q=[]
  level[v]=0
  q.append(v)
  while len(q)>0:
    j=q.pop(0)
    for k in AList[j]:
      if level[k]==-1:
        level[k]=level[j]+1
        parent[k]=j
        q.append(k)

  return level,parent

def minimumhops(AList, start, end):
  level, path=BFSListLevelPath(AList, start)
  shortestpath = []
  if level[end]!=-1:
    shortestpath.append(end)
    while shortestpath[-1]!=start:
      end = path[end]
      shortestpath.append(end)
  else:
    shortestpath.append(start)
  return shortestpath[::-1]