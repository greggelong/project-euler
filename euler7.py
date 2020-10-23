## brute forced with out optimization in 0:00:44.550140 on dell and 2min24 seconds on pydroid
## brute forced with optimization 0:00:00.311020 0.8 seconds

from datetime import datetime
import math

def isprime(n):
    if n==1:
        return False
    if n==2:
        return True
    else:
        # with out optimization for i in range(2,n)
        for i in range(2,1+math.floor(math.sqrt(n))):  ## but with optimizatioin sqr
            if n%i==0:
                return False
        return True


startTime = datetime.now()
print('#'*5,isprime(2))     
pcount =0
num=1
while pcount<10001:
    num=num+1
    if isprime(num):
        pcount+=1
        #print(pcount,n);
                

        
print('#'*5,pcount,num)
print(datetime.now() - startTime)               
                    