import numpy as np
def bellmanfordalgo(VMAT,s):
  (rows,cols,x)=VMAT.shape
  infinity= np.max(VMAT)+rows+1
  distance={}
  for v in range(rows):
    distance[v]=infinity

  distance[s]=0

  for i in range(rows):
    for u in range(rows):
      for v in range(cols):
        if VMAT[u,v,0]==1:
          distance[v]=min(distance[v],distance[u]+VMAT[u,v,1])

  return distance

def bellmanfordlist(VMat,s):
  infinity=1+len(VMat.keys())+max([d for u in VMat.keys() for (v,d) in VMat[u]])

  distance={}
  for i in VMat.keys():
    distance[i]=infinity

  distance[s]=0

  for i in VMat.keys():
    for u in VMat.keys():
      for (v,d) in VMat[u]:
        distance[v]=min(distance[v],distance[u]+d)

  return distance
  