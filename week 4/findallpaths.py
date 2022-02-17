vertices=[1,2,3,4,5,6,7,8]
gList={1:[3,4],2:[3],3:[6],4:[6,7],5:[4,6],6:[2],7:[5]}
source=1
destination=2
walkedPath=[]
startingList=[]

for key,value in gList.items():
  if(source==key):
    walkedPath.append(key)
    startList=value
    break

while(len(startList)>0):
    temp=startList.pop()
    nextList=gList[temp]
    for j in nextList:
      walkedPath.append(j)
      #startList.append(j)




print(walkedPath)



  





