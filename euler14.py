'''
##### 837799 525
0:00:19.302845
'''

from datetime import datetime

def colatz(num):
    savenum = num
    count=0
    while num != 1:
        #print('#'*5,num)
        if num %2==0:
            num=num//2
            count+=1
        else:
            num=num*3+1
            count+=1
        
    #print('#'*5,1)
    
    return savenum, count+1


print('#'*5,colatz(1))


startTime = datetime.now()
highcount=0
longcolatz=0
for i in range(2,1000000):
    colatznum,count = colatz(i)
    if count > highcount:
        highcount = count
        longcolatz = colatznum

print('#'*5, longcolatz, highcount)

print(datetime.now() - startTime)