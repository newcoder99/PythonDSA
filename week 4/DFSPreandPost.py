(visited,pre,post)=({},{},{})

def DFSInitPreAndPost(AList):
  
  for i in AList.keys():
    visited[i]=False
    (pre, post)=(-1, -1)
  
  return

def DFSPrePost(AList,v,count):
  visited[v]=True
  pre[v]=count
  count=count+1
  for k in AList[v]:
    if(not visited[k]):
      parent[k]=v
      count=DFSPrePost(AList,v,count)
  post[v]=count
  count=count+1
  return(count)

