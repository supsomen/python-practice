lst=[]
n=int(input())
for i in range(n):
    a=int(input())
    lst.append(a)
print(lst)
b=int(input())
for i in range(len(lst)):
    print(lst[i])
    if(lst[i]==b):
        del lst[i]
        break
print(lst)    
    
