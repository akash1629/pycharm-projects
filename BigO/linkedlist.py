class node:
     def __init__(self,value):
         self.value=value
         self.next=None



class LinkedList:
     def __init__(self,value):
         new_node = node(value)
         self.head=new_node
         self.tail=new_node

newll=LinkedList(10)
print(newll.head.value)