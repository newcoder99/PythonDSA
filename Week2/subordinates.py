L=[194, 69, 103, 150, 151, 44, 103, 98]

def subordinates(L):
  for i in range(0,len(L)):
    for j in range(0,len(L)):
      if(L[i]<L[j]):
        temp=L[j]
        L[j]=L[i]
        L[i]=temp
  
  count=0
  M=L
  for i in range(0,len(L)):
    M=L    
    M=M[2:]
    count=count+1
    print(count)
    
  return (M,count)

print(subordinates(L))