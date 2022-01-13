def expanding(L):
  previousdiff=0
  for i in range(0,len(L)-1):
    currentdiff=abs(L[i+1]-L[i])
    if(i==0):
      previousdiff=currentdiff
    else:
      if(currentdiff>previousdiff):
        previousdiff=currentdiff
        continue
      else:
        return False    
  return True

L = eval(input())
print(expanding(L))