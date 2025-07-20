class queue:
    def __init__(self):
        self.list=[]
#to convert list element into string
    def __str__(self):
        value=[str(x) for x in self.list]     #this will make list into list of string element due to str
        return ",".join(value)

    def enqueue(self):