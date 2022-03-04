class Queue:
    def __init__(self):
        self.queue = []

    def addq(self,v):
        self.queue.append(v)

    def delq(self):
        v = None
        if not self.isempty():
            v = self.queue[0]
            self.queue = self.queue[1:]
        return(v)
    
    def isempty(self):
        return(self.queue == [])

    def __str__(self):
        return(str(self.queue))
        
def longJourney(AList):
    (indegree,lpath,length) = ({},{},{})
    for u in AList.keys():
        (indegree[u],lpath[u],length[u]) = (0,0,[])
    
    for u in AList.keys():
        for v in AList[u]:
            indegree[v] = indegree[v] + 1
    zerodegreeq = Queue()
    for u in AList.keys():
        if indegree[u] == 0:
            zerodegreeq.addq(u)
    while (not zerodegreeq.isempty()):
        j = zerodegreeq.delq()
        indegree[j] = indegree[j]-1
        for k in AList[j]:
            if len(length[j])==0:
                length[k].append([j])
            else:
                for y in range(len(length[j])):
                    length[k].append(length[j][y]+[j])
            indegree[k] = indegree[k] - 1
            lpath[k] = max(lpath[k],lpath[j]+1)
            if indegree[k] == 0:
                zerodegreeq.addq(k)
    max2=-10
    for key, value in lpath.items():
        if value>max2:
            max2=value
            key2=key
    if max2==0:
        return([key2])
    return(length[key2][-1]+[key2])