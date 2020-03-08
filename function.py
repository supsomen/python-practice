def sum():
    value=0
    lst=[]
    n=int(input())
    for i in range(n):
        a=int(input())
        lst.append(a)
    print(lst)
    for j in lst:
        value=value+j
    return value
print(sum())
def string():
    n=str(input())
    a=n[::-1]
    return a
print(string())
def fact():
    n=int(input())
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
print(fact())
def upper():
    a=input()
    count=0
    for i in a:
        if(i.isupper()):
           count=count+1
    return count
print(upper())
def lower():
    b=input()
    count=0
    for i in b:
        if(i.islower()):
            count=count+1
    return count
print(lower())
def even():
    lst=[]
    n=int(input())
    for i in range(n):
        a=int(input())
        lst.append(a)
    lst1=[]
    for j in lst:
        if(j%2==0):
            lst1.append(j)
            
    return lst1
print(even())
def prime():
    n =int(input())
    flag=0
    if(n>1):
       for i in range(2,n):
           if(n%i==0):
               flag=1
               break 
    if(flag==1):
        print("not prime")
    else:
        print("prime")
prime()
    

