def prime_product(n):
  lstFactors=[]
  for i in range(2,n):
    if(n%i==0):
      lstFactors.append(i)

  lstPrimeFactors=[]
  for i in lstFactors:
    isPrime=True   
    if(i==2):
      lstPrimeFactors.append(i)
      continue 
    for j in range(2,i):
      if(i%j==0):
        isPrime=False
        break
      else:
        continue
    if(isPrime==True):
          lstPrimeFactors.append(i)   

  number=1
  for i in lstPrimeFactors:
    number=number*i

  if(number==n):
    return True
  else:
    return False

n = int(input())
print(prime_product(n))