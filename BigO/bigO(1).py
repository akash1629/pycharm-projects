from array import array
my_array=array("i",[1,2,3,4,5,])
print(my_array)
print(len(my_array))
print(my_array.insert(0,0))
print(my_array)

def traverse(arra):
    for i in arra:
        print(i)

traverse(my_array)

def access(array1):
    print(array1[0:])

access(my_array)

def search_array(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
