def reverse(root):
    nextAdd=root.next
    previous=root
    root.next=None
    while(nextAdd!=None):
        temp=nextAdd.next
        nextAdd.next=previous
        previous=nextAdd
        nextAdd=temp
        
    return previous