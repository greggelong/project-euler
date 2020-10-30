from datetime import datetime



def isprime(n):
    if n==1:
        return False
    elif n==2:
        return True
    
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i == 0:
                return False
            
    return True

starttime = datetime.now()    
#sum of primes    
sum=2    # start with 2 
for p in range(3,2000000,2):  #check only odd numbers after that
    if isprime(p):
        sum+=p
        
print('the sum is', sum)
print(datetime.now()-starttime)