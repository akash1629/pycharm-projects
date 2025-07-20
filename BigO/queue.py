class queue:
    def __init__(self):
        self.list=[]
#to convert list element into string
    def __str__(self):
        value=[str(x) for x in self.list]     #this will make list into list of string element due to str
        return ",".join(value)               #i need to print values , but instead of print(value) this will join them via ,

    def isEmpty(self):
        if self.list==[]:
            return True
        else:
            return False

    def enqueue(self,value):  #enqueue will take value from us and append it in self.list
        self.list.append(value)


customQueue=queue()
customQueue.enqueue(4)
customQueue.enqueue(3)
customQueue.enqueue(2)
print(customQueue)
