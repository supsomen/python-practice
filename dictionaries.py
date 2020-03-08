name={}
for i in range(2):
    key=input()
    value=input()
    name[key]=value
print(name)
name[3]='hemant'
print(name)
dic1={1:10,2:20,3:30}
dic2={4:40,5:50}
dic3={}
for d in (dic1,dic2):dic3.update(d)
print(dic3)
d={}
for i in range(3):
    key=input()
    value=input()
    d[key]=value
print(d)    
key=input()
if key in d.keys():
    print("key is present")
else:
    print("not present")
for key in d:
    print(key)
for i in d:
    print(d[i])
print(key)
print(d[i])
d={}
for i in range(15):
    d[i]=i*i
print(d)    
d={}
sum=0
for i in range(5):
    value=input()
    d[i]=int(value)
    sum=sum+value
print(sum)    
