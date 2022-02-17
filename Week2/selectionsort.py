def selectionSort(L):
  if(len(L)==0 or len(L)==1):
    return L
  for step in range(len(L)):
    min_idx = step

    for i in range(step + 1, len(L)):
        if L[i] < L[min_idx]:
           min_idx = i
    (L[step], L[min_idx]) = (L[min_idx], L[step])


  return L


L=[3,4,1,2,5]
print(selectionSort(L))