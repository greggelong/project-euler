# list comprehension

sqrs = [x**2 for x in range(1,101)]
print('#'*5,sqrs,sum(sqrs))
sqrssum=sum(sqrs)
sums =sum(list(range(1,101)))
print('#'*5,sums,sums **2)
sumssqr=sums**2

result =sumssqr-sqrssum
print('#'*5, result)