def sumsquare(L):
  sumOdd=0
  sumEven=0
  for i in range(0,len(L)):
    if(L[i]%2==0):
      sumEven=sumEven+L[i]*L[i]
    else:
      sumOdd=sumOdd+L[i]*L[i]
    
  return [sumOdd,sumEven]


L = eval(input())
print(sumsquare(L))