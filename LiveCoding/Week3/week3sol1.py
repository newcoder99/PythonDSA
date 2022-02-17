class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.head = None
        self.last = None

    def Enqueue(self,data):
      if self.last is None:
         self.head = Node(data)
         self.last = self.head
      else:
         self.last.next = Node(data)
         self.last = self.last.next


    def Dequeue(self):
      if self.head is None:
         return None
      else:
         val_returned = self.head.data
         self.head = self.head.next
         return val_returned

L=[1,2,3,4,5]
r=3

n=Node(3)
q=Queue()

for i in L: 
  q.Enqueue(i)
  
for i in L: 
  print(q.Dequeue())

print(L)