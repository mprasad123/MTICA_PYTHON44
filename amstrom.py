import math
n=int(input())
total=0
for i in n:
    total+=math.pow(int(i),int(n))
if n==total:
     print(n,"is amstarm")
 else:
        print(n,"is not amstram")
        
