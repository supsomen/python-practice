from sys import argv
sum=0
for i in range(1,len(argv)):
	n=int(argv[i])
	
	if(n>1):	
		flag=0
		for j in range(2,n):
			if(n%j==0):
				flag=1
				break
		if(flag==0):
			sum=sum+n
print(sum)			


