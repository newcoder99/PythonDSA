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
  
def topLogSort(AMat):
  (rows,cols)=AMat.shape
  indegree={}
  toposortList=[]

  for c in range(cols):
    indegree[c]=0
    for j in range(rows):
      if(AMat[j,c]==1):
        indegree[c]=indegree[c]+1

  
  for i in range(rows):
    j=min([k for k in range(cols) if indegree[k]==0])
    toposortList.append(j)
    indegree[j]=indegree[j]-1
    for k in range(cols):
      if(AMat[j,k]==1):
        indegree[j]=indegree[j]-1



  return(toposortList)

def topLogSortList(AList):
  (rows,cols)=AList.shape
  indegree={}
  toposortList=[]

  for u in AList.keys():
    for v in AList[u]:
      indegree[v]=indegree[v]+1


  zerodegreeq=Queue()
  for u in AList.keys():
    if(indegree[u]==0):
      zerodegreeq.addq(u)

  while(not zerodegreeq.isEmpty()):
    j=zerodegreeq.delq()
    toposortList.append(j)
    indegree[j]=indegree[j]-1
    for k in AList[j]:
        indegree[k]=indegree[k]-1
        if(indegree[k]==0):
          zerodegreeq.addq(k)

   return(toposortList)