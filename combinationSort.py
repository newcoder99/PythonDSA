def combinationSort(strList):
  L1=[]
  L2=[]
  Firstcharacters=[]
  for i in range(0,len(strList)):
    Firstcharacters.append(strList[i][0])
  d={}
  e={}
  for i in Firstcharacters:
        if i in d.keys():
            d[i]+=1
        else:
            d[i]=1
  for key in sorted(d):
    e[key]=d[key]  

  for i in e:
    if(e[i]==1):
      for j in range(0,len(strList)):
        if(i==strList[j][0]):
          L1.append(strList[j])
          break
    elif(e[i]>1):
      temp=[]
      for j in range(0,len(strList)):
        if(i==strList[j][0]):
          temp.append(int(strList[j][1:]))
      
      for l in temp:
        L1.append(i+str(l))

  
  
  for i in e:
    if(e[i]==1):
      for j in range(0,len(strList)):
        if(i==strList[j][0]):
          L2.append(strList[j])
          break
    elif(e[i]>1):
      temp=[]
      for j in range(0,len(strList)):
        if(i==strList[j][0]):
          temp.append(int(strList[j][1:]))
      
      temp.sort(reverse=True)
      for l in temp:
        L2.append(i+str(l))

  return (L1,L2)