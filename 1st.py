import math
def checkprime(n):
    if n<1:
        return 0
    if n==1 or n==2 or n==3:
         return n
    count=n//2+1
    for i in range (2,count+1):
         if n%i==0:
             return 0
    return n
f=int(input())
l=int(input())
lis=[]
for j in range(f,l+1):
    if checkprime(j):
        lis.append(j)
 print(*lis)
print(len(lis))
        
