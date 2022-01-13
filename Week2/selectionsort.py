
def selectionsort(A):
    if(len(A)==0 or len(A)==1):
      return A
    for i in range(0,len(A)):
      for j in range(0,len(A)):
        if(A[i]<A[j]):
          (A[i],A[j])=(A[j],A[i])
    return A

A=[1,4,2,3]
print(selectionsort(A))