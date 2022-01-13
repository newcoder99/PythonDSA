def mergeInPlace(A,B): 
  
  for i in range(0,len(A)):
    for j in range(0,len(B)):
      if(A[i]> B[j]):
        A.swap(i,B,j)
  
  for i in range(0,len(B)):
      for j in range(i,len(B)):
          
          if(B[i]>B[j]):
              B.swap(i,B,j)