#No negative edges
import numpy as np
#using Matrix
def dijkstra(VMat,s):
  (rows,cols,x)=VMat.shape()
  infinity=np.max(VMat)*rows+1
  (visited,distance)=({},{})
  for i in range(rows):
    (visited[i],distance[i])=(False,infinity)

  distance[s]=0
  for i in range(rows):
    nextd=min([distance[v] for v in range(rows) if not visited[v]])

    nextvList=[v for v in range(rows) if(not visited[v] and distance[v]==nextd)]

    if nextvList==[]:
      break
    nextv=min(nextvList)
    visited[nextv]=True
    for v in range(cols):
      if(VMat[nextv,v,0]==1) and not visited[v]:
        distance[v]=min(distance[v],distance[nextv]+VMat[nextv,v,1])

  return distance

#using Adjacency List
def dijstraaList(VList,s):
  infinity=1+len(VList.keys())+max([d for u in VList.keys() for (v,d) in VList[u]])
  (visited,distance)=({},{})
  for i in VList.keys():
    (visited[i],distance[i])=(False,infinity)

  for j in VList.keys():
    nextd= min([distance[v] for v in VList.keys() if not visited[v]])

    nextVList =  [v for v in VList.keys() if( not visited[v] and distance[v]==nextd)]

    if nextVList==[]:
      break
    nextv=min(nextVList)
    visited[nextv]=True
    for (v,d) in VList[nextv]:
      if not visited[v]:
        distance[v]=min(distance[v],distance[nextv])

  return distance