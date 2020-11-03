from datetime import datetime

def countFactors(n):
    '''
  big duh-doy I only need to check to the square root of the number
  and then count by two since every number below the sqrt has it corrisponding
  number above the sqrt.
  if done without this optimization (just checkting range (1, n+1)it was taking close to a day
  with the optimization it took just about 10 seconds:
  12375 76576500 576
nth 12375 triNum 76576500 n factors 576
0:00:10.049704
  

'''
    count = 0
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            count = count + 2
    return count


def triNum(n):
    result = 0
    for i in range(1, n+1):
        result = result + i
    return result
        

starttime = datetime.now() 
goal = 0
num = 0
while goal < 501:
    #print(num)
    num = num +1
    a = triNum(num)
    
    b = countFactors(a)
    #print("triNum", a, "factors",b , "highest", goal)
    if b > goal:
        goal = b
        print(num ,a ,  goal)
    
    
print("nth", num, "triNum", a, "n factors", goal);    
    
print(datetime.now()-starttime)