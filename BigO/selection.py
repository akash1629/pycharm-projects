# def selec(clist):
#     for i in range(len(clist)):
#         min=i
#         for j in range(i+1,len(clist)):
#             if clist[j]< clist[min]:
#                  min=j
#
#         clist[i],clist[min]=clist[min],clist[i]
#
#
#     return clist


# def insertion(cli):
#     for i in range(1, len(cli)):
#         j=i
#         while j>0 and cli[j]<cli[j-1]:
#             cli[j],cli[j-1]=cli[j-1],cli[j]
#             j-=1

    # return cli

def divide(li):
    if len(li) <= 1:  # <-- Base case to stop recursion
        return li
    mid=len(li)//2
    left=li[:mid]
    right=li[mid: ]
    left=divide(left)
    right=divide(right)
    return merge(left,right)

def merge(left,right):
     i, j = 0, 0
     result = []
    while i<len(left) and j<len(right):

       if left[i]>right[j]:
          result.append(right[j])
          j+=1
       else:
           result.append(left[i])
           i+=1
    return result

custom=[5,7,2,1]
sor=divide(custom)
print(sor)