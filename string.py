lst=[]
n=int(input())
for i in range(n):
    a=input()
    lst.append(a)
print(lst)
count =0
for i in lst[0]:
    if i.isupper():
        count=count+1
print(count)
sum=0
for i in lst[0]:
    if i.islower():
        sum=sum+1
print(sum)
s1=input()
s2=s1[::-1]
if(s2==s1):
    print("palimdrome")
else:
    print("not palimdrome")
a=input()
n=len(a)
for i in range(n):
    print(a[0:2],end="")
d=input()
n=len(d)
b=str(input())
for i in range(n):
   if(d[0]==b and d[n-1]==b):
         print(d.replace(b,""))
         break
   else:
         print(d)
         break
s8=input()
n=int(input())
for i in range(n):
    print(s8[-n:],end="")
