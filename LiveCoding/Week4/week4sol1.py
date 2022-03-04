class Indegree:
    def __init__(self):
        self.ind_list = {}
        self.ind_mat = {}
    def Indegree_List(self,GList):
      IndegreeDict={}
      for key,value in GList.items():
        if(key not in IndegreeDict):
            IndegreeDict[key]=0
        for i in value:
          if(i not in IndegreeDict):
            IndegreeDict[i]=1
          else:
            IndegreeDict[i]=IndegreeDict[i]+1
      
      return IndegreeDict
    
    def Indegree_Mat(self,GMat):
      IndegreeDict={}
      for i in range(0,len(GMat)):
        for j in range(0,len(GMat[i])):
          if(j not in IndegreeDict.keys()):
            IndegreeDict[j]=0
          if(GMat[i][j]==1):
            IndegreeDict[j]=IndegreeDict[j]+1
          
      return IndegreeDict
GList=eval(input())
GMat = eval(input())
G = Indegree()
IGL = G.Indegree_List(GList)
IGM = G.Indegree_Mat(GMat)
print('For adjacency list')
for i in range(len(GList)):
    print(i,' = ',IGL[i])
print('For adjacency matrix')
for i in range(len(GMat)):
    print(i,' = ',IGM[i])