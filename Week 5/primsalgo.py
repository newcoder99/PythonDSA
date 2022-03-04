def primlist(Vmat):
  infinity = 1+max([d for u in Vmat.keys() for (v,d) in Vmat[u]])
  (visited,distance,TreeEdges)=({},{},[])
  for v in Vmat.keys():
    (visited[v],distance[v])=(False,infinity)
  visited[0]=True
  for (v,d) in Vmat[0]:
    distance[v]=d
  for i in Vmat.keys():
    (mindist,nextv)=(infinity,None)
    for u in Vmat.keys():
      for (v,d) in Vmat[u]:
        if visited[u] and (not visited[v]) and d<mindist:
          (mindist,nextv,nexte)=(d,v,(u,v))

    if nextv in None:
      break

    visited[nextv]=True
    TreeEdges.append(nexte)
    for (v,d) in Vmat[nextv]:
      if not visited[v]:
        distance[v]=min(distance[v],d)

  return TreeEdges

def primlist2(Vmat):
  infinity = 1+max([d for u in Vmat.keys() for (v,d) in Vmat[u]])
  (visited,distance,nbr)=({},{},{})
  for v in Vmat.keys():
    (visited[v],distance[v],nbr[v])=(False,infinity,-1)
  visited[0]=True
  for (v,d) in Vmat[0]:
    (distance[v],nbr[v])=(d,0)
  for i in range(1,len(Vmat.keys())):
    nextd=min([distance[v] for v in Vmat.keys() if not visited[v]])

    nextvlist = [v for v in Vmat.keys() if (not visited[v] and distance[v]==nextd)]

    if nextvlist==[]:
      break
    nextv=min(nextvlist)
    visited[nextv]=True
    for (v,d) in Vmat[nextv]:
      if not visited[v]:
        (distance[v],nbr[v])=(min(distance[v],d),nextv)

  return nbr