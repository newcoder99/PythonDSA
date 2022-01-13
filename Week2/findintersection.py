def findIntersection(set1, set2):
    lst=[]
    for i in set1:
      for j in set2:
        if(i==j):
          lst.append(i)
          break
    
    return lst

set1 = [1,2,3,5]
set2 = [2,3]
result = findIntersection(set1, set2)
result.sort()
print(*result)