def sortInRange(L,r):
    d={}
    for i in L:
        if i in d.keys():
            d[i]+=1
        else:
            d[i]=1
    L.clear()
    for i in range(r):
        L.extend([i]*d[i])

L=[2,3,4,-5,1]


def findLargest(L):
  low=0
  high=len(L)-1
  if(len(L)==0):
    return
  if(L[low]==L[high] and len(L)==1):
    return L[high]
  elif(L[low]<L[high] and len(L)>1):
    return L[high]
  elif(L[low]>=L[high]):
    while(True):
      high=low 
      low=low+1
      if(L[low]>=L[high]):
        continue
      elif(L[low]<L[high]):
        return L[high]
    

      
print(findLargest(L))