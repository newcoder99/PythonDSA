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


def longestPath(AList):
  (indegree,lpath)=({},{})
  for u in AList.keys():
    (indegree[u],lpath[u])=(0,0)
  for u in AList.keys():
    for v in AList[u]:
      indegree[v]=indegree[v]+1

  zerodegreeq=Queue()
  while(not zerodegreeq.isempty()):
    j=zerodegreeq.delq()
    indegree[j]=indegree[j]-1
    for k in AList[j]:
      indegree[k]=indegree[k]-1
      lpath[k]=max(lpath[k],lpath[j]+1)
      if indegree[k]==0:
        zerodegreeq.addq(k)

  return lpath   