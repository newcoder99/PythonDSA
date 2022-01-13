def findLargest(L):
  left=0
  right=len(L)-1
  while (left < right):
      mid = left + int((right - left) / 2);
      if (L[left] < L[mid]):
            left = mid;
      elif (L[left] > L[mid]): 
            right = mid - 1;
      else:    
            left = left + 1;      
            
  return L[left];