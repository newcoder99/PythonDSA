class Queue:
  
  def __init__(self):
    self.queue=[]
  
  def addq(self,v):
    self.queue.append(v)

  def isEmpty(self):
    return [self.queue==[]]
  
  def __str__(self):
    return(str(self.queue))

  def delq(self):
    v=None
    if(self.queue.isEmpty()):
      v=self.queue[0]
      self.queue=self.queue[1:]
    return v
  

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

def Components(AList):
  component={}
  for i in AList.keys():
    component[i]=-1

  (compid,seen)=(0,0)

  while seen<=max(AList.keys()):
    startv=min([i for i in AList.keys() if component[i]==-1 ])

    visited=BFSListPath(AList,startv)
    for i in visited.keys():
      if visited[i]:
        seen=seen+1
        component[i]=compid
    compid=compid+1

  return (component)    