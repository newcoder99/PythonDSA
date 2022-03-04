def Krushal(WList):
  (edges,component,TE)=([],{},[])
  for u in WList.keys():
    #Weight as first component sorts easily
    edges.extend([(d,u,v) for (v,d) in WList[u]])
    component[u]=u

  edges.sort()
  print(edges)

  for (d,u,v) in edges:
    if component[u]!=component[v]:
      TE.append(u,v)
      c=component[u]
      for w in WList.keys():
        if component[w]==c:
          component[w]=component[v]

  return TE
    