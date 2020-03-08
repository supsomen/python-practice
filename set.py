l=[]
n=int(input())
for i in range(n):
    a=input()
    l.append(a)
print(l)
l.sort()
print(l)
t=tuple(l)
print(t)
s=set(t)
print(s)
b=input()
s.remove(b)
print(s)
x=set(["blue","green","red"])
y=set(["yellow","blue","pink"])
z=x & y
print(z)
w=x | y
print(w)
l=[]
n=int(input())
for i in range(n):
    a=int(input())
    l.append(a)
print(l)
t=tuple(l)
print(t)
s=set(t)
print(s)
print(max(s))
print(min(s))
    
