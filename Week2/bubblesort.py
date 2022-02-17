def bubblesort(L):
  if(len(L)==0 or len(L)==1):
    return L
  
  for i in range(0,len(L)):
    for j in range(len(L)-i-1):
      if(L[j]>L[j+1]):
        (L[j],L[j+1])=(L[j+1],L[j])


  return L

L=[3,4,6,1,2]
print(bubblesort(L))