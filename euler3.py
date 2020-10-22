def primeFactors(n):
	#print the numbet of 2s thay divide in
	while n%2 == 0:
		print('*'*5,2,n)
		n=n//2
		
	#must be odd
	for i in range(3,n//2,2):
		
		#whil i divides in reduce
		while n%i==0:
			print('*'*5,i,n)
			n=n//i
			
	if n >2:
		print('*'*5,n)
		
		
n= int(input('  input an interger '))

primeFactors(n)	