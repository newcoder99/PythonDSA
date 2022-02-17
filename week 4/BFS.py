class Queue:
  def __init__(self):
    self.queue=[]

  def addqueue(self,v):
    self.queue.append(v)
  
  def isempty(self):
    return (self.queue==[])

  def delqueue(self):
    v=None
    if not self.isempty():
      v = self.queue[0]
      self.queue=self.queue[1:]
    return v

  def __str__(self):
    return(str(self.queue))

  def neighbours(AMat,i):
    nbrs=[]
    (rows,cols)=(AMat.shape)
    for j in range(cols):
      if AMat[i,j]==1:
        nbrs.append(j)
    return nbrs


  def BFS(AMat,v):
    (rows,cols)=(AMat.shape)

    visited= {}

    for i in range(rows):
      visited[i]=False

    q=Queue()

    visited[v]=True
    q.addqueue(v)

    while(not q.isempty()):
      j=q.delqueue()
      for j in q.neighbours(AMat,v):
        if not visited[j]:
          visited[j]=True
          q.addqueue(j)

    return visited
  
  #Using Adjacency List for this
  def BFSListPath(AList,v):
    (visited,parent)=({},{})
    for i in AList.keys():
      visited[i]=False
      parent[i]=-1

    q=Queue()
    visited[v]=True
    q.addq(v)

    while(not q.isempty()):
      j=q.delqueue()
      for k in AList[j]: 
        if(not visited[k]):
          visited[k]=True
          parent[k]=j
          q.addq(k)
    
    return (visited,parent)


  #BFS to record distance
  def BFSListPathLevel(AList,v):
    (level,parent)=({},{})
    for i in AList.keys():
      level[i]=-1
      parent[i]=-1

    q=Queue()
    level[v]=-1
    q.addq(v)

    while(not q.isempty()):
      j=q.delqueue()
      for k in AList[j]: 
        if(level[k]==-1):
          level[k]=level[k]+1
          parent[k]=j
          q.addq(k)
    
    return (level,parent)
