def insertionSort(L):
  if(len(L)==0 or len(L)==1):
    return L

  for i in range(1,len(L)):

    key_item=L[i]

    j=i-1

    while(j>=0 and L[j]>key_item):
      L[j+1]=L[j]
      j=j-1

    L[j+1]=key_item
  

  return L

    

L=[3,4,1,2,5]
print(insertionSort(L))