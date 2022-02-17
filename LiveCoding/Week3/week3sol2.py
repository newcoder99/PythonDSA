class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class doubly_linked_list:
    def __init__(self):
        self.head = None
        self.last = None
      
    def insert_end(self,data):
        newnode = Node(data)
        newnode.prev = self.last
        if self.head == None:            
            self.head = newnode
            self.last = newnode
        else:
            self.last.next = newnode
            self.last = newnode
    def insert_at_pos(self,data,pos):
      newnode=Node(data)
      count=1
      if self.head == None:            
          self.head = newnode
          self.last = newnode
      else:
          temp=self.head
          while(count<pos-1):
            temp=temp.next
            count=count+1
            
          if(temp != None):
              newnode.next = temp.next
              newnode.prev = temp
              temp.next = newnode  
              if (newnode.next != None):
                newnode.next.prev = newnode