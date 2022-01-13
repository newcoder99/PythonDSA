
students=[("ramesh",5),("sita",4),("suresh",6),("gita",8),("ganesh",1)]

def sortTuples(students):

  lst=[]
  for i in range(0,len(students)):
    lst.append(students[i][1])
  
  for i in range(0,len(lst)):
    for j in range(0,len(lst)):
      if(lst[i]<lst[j]):
        temp=lst[i]
        lst[i]=lst[j]
        lst[j]=temp

  for i in range(0,len(lst)):
    for j in range(0,len(students)):
      if(students[i][1]<students[j][1]):
        temp=students[i]
        students[i]=students[j]
        students[j]=temp
      

sortTuples(students)