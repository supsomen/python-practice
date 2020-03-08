list=[]
n=int(input())
for i in range(n):
    a=input()
    list.append(a)
print(list)
tup=tuple(list)
print(tup)
print(tup[3])
print(tup[-4])
b=input()
if b in tup:
    print("present")
else:
    print("not present")
c=input()
index=tup.index(c)
print(index)
l=[(20,30,40),(50,60,70),(70,80,90)]
print([t[:-1]+(100,) for t in l])
