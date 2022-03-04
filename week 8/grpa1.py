def findOccOf(L, x):
  startLocation = None
  endLocation = None
  for i in range(0,len(L)):
    if L[i]==x and startLocation is None:
      startLocation=i
    else:
      endLocation = i

  if startLocation is None:
    return (None,None)
  else:
    return (startLocation,endLocation)
      
    
  