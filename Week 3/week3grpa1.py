def DishPrepareOrder(L):
  d={}
  
  for i in range(0,len(L)):
    if(L[i] not in d):
        d[L[i]]=1
    else:
      d[L[i]]=d[L[i]]+1

  l=dict(sorted(d.items(), key=lambda item: item[1],reverse=True))
  F={}
  m=[]
  for i in l:    
    if(l[i] not in F):
        m=[]
        m.append(i) 
        F[l[i]]=m   
    else:
      m.append(i) 
      F[l[i]]=m
   
  m=[]
  for i in F:
    F[i].sort()
    m=m+F[i]
  
  return m
nums = eval(input())
print(DishPrepareOrder(nums))