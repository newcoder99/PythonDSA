def binarySearchIndexAndComparisons(L,k):
    low=0
    high=len(L)-1
    mid=0
    count=0
    while low<=high:      
      mid = (low+high)//2
      count=count+1
      if(L[mid]<k):        
        low=mid+1      
      elif(L[mid]>k):
        high=mid-1
      else:
        return (True,count) 
    return (False,count)
