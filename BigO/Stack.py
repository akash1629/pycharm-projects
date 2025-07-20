class stack:
    def __init__(self):
        self.list=[]

    def __str__(self):
        return str([x for x in reversed(self.list)])


    def push(self,value):
        self.list.append(value)
        return"successfull"


customStack=stack()
customStack.push(4)
customStack.push(3)
customStack.push(2)
print(customStack)
