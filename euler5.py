#  brute force takes about 0:00:08.402587 seconds on dell and 13.3 seconds on pydroide
# without printing

from datetime import datetime


def isdivby(n):
    for i in range(2,20+1):
        if n%i != 0:
            return False
    return True
    
    
print (isdivby(2520))


startTime = datetime.now()
result = 0
itnum=20
while result == 0:
    if isdivby(itnum):
        result = itnum
    itnum+=20 # its got to be div by 20
    #print('#'*5,itnum) # dont print it slows it
        
        
print('#'*7,result)
print(datetime.now() - startTime)
