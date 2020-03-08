def even():
    lst=[]
    n=input()
    for i in range(n):
        a=input()
        lst.append(a)
    lst1=[]
    for j in lst:
        if(j%2==0):
            lst1.append(j)
            print(lst1)
    return lst1
    print(even())
     
