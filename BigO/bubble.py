def bubble(clist):
    for i in range(len(clist)-1):
        for j in range(len(clist)-1):
            if clist[j] > clist[j+1]:
                clist[j],clist[j+1]=clist[j+1],clist[j]

    return clist

custom=[5,7,2,8,1]
sor=bubble(custom)
print(sor)
