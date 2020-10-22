

def fibit(n):
	sum =0
	fib =[0,1]
	for i in range(2,n+1):
		nextfib = fib[len(fib)-1] +fib[len(fib)-2]
		fib.append(nextfib)
		if nextfib%2==0:
			sum+=nextfib
	return fib, sum
	
	
def fibit2(n):
	sum =0
	fibminus1=1
	fibminus2=0
	for i in range(2,n+1):
		nextfib = fibminus1 +fibminus2
		#print('#'*8, nextfib)
		if nextfib%2==0:
			sum+=nextfib
		fibminus2 = fibminus1
		fibminus1 = nextfib	
			
	return sum
	
def fibit3():
	sum =0
	fibminus1=1
	fibminus2=0
	nextfib=0
	while nextfib<4000000:
		nextfib = fibminus1 +fibminus2
		print('#'*8, nextfib)
		if nextfib%2==0:
			sum+=nextfib
		fibminus2 = fibminus1
		fibminus1 = nextfib	
			
	return sum
	
		
			
print('#'*8,fibit(33))	
print('#'*8,fibit2(33))
print('#'*8,fibit3())				