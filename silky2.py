from sys import argv
c=int(argv[1])
print(argv[2])
d = c
sum=0
while(c!=0):
    x=c%10
    sum=sum*10+x
    c=c//10
print(sum)
if(d==sum):
    print("Palimdrome")
else:
    print("Not Palimdrome")
