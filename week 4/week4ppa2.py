ans=[]
class Queue:
  def __init__(self):
    self.queue=[]
  
  def addq(self,v):
    self.queue.append(v)

  def isempty(self):
    return (self.queue==[])

  def delq(self):
    v=None
    if(not self.queue.isempty()):
      v=self.queue[0]
      self.queue=self.queue[1:]
    
    return v
  
  def __str__(self):
    return(str(self.queue))

def findPath(alist, source, dest, visited, path):

  visited[source]=True
  path.append(source)

  if source==dest:
    ans.append(''.join(path))
  else:
    for i in alist[source]:
      if(visited[i]==False):
        findPath(alist, i, dest, visited, path)

  path.pop()
  visited[source] = False
  

def findAllPaths(v,gList,source,destination):
  vertices={}
  for i in v:
    vertices[i]=False

  path=[]
  findPath(gList,source,destination,vertices,path)

  return ans
#Vertices are expected to be labelled as single letter or single digit 

#Sort and arrange the result for uniformity
def ArrangeResult(result):
  res = []
  for item in result:
    s = ""
    for i in item:
      s += str(i)    
    res.append(s)
  res.sort() 
  return res

v = [item for item in input().split(" ")]
Alist = {}
for i in v:
  Alist[i] = [item for item in input().split(" ") if item != '']
source = input()
dest = input()
print(ArrangeResult(findAllPaths(v, Alist, source, dest)))