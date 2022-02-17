from  itertools import chain
def findComponents_undirectedGraph(vertices,edges):
    lst=[]
    d={}
    for i in range(0,len(vertices)):
      d[vertices[i]]=False
    temp=[]
    for i in range(0,len(edges)):
      if(i==0): 
        temp=[]   
        temp.append(edges[i][0])
        temp.append(edges[i][1])
        prev=edges[i][0]
        nextV=edges[i][1]
        continue  
      if(prev==edges[i][0] or prev==edges[i][1] or nextV==edges[i][0] or nextV==edges[i][1]):  
        temp.append(edges[i][1])        
        prev=edges[i][0]
      else:
        if(temp not in chain(*lst)):
          lst.append(temp) 
        elif(i==len(edges)-1):               
           temp.append(edges[i][0])
           temp.append(edges[i][1])
           lst.append(temp) 
        prev=edges[i][0]
        temp.append(edges[i][0])
        temp.append(edges[i][1])
    
       
    length=len(lst)
    for i in range(0,len(lst)):
      for j in range(0,len(lst[i])):
        if(lst[i][j] in vertices):
          vertices.remove(lst[i][j])

    
    if(len(vertices)==0):
      length=1
    if(len(vertices)>0):   
      length=len(lst)+len(vertices)
      
    return length