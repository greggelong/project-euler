def diaphant(m,n):
    ## m is larger
    a = m**2 - n**2
    b = 2*(m*n)
    c = m**2+n**2
    return a, b, c


print(diaphant(2,1))

print(sum(diaphant(2,3)))

for mm in range(1,500):
    for nn in range(1,500):
        aa,bb,cc = diaphant(mm,nn)
        if aa+bb+cc == 1000 and aa >0 and bb>0 and cc>0: ##will have neg sol too 
            print("p trp that adds up to 1000 is: a, b, c: ",aa,bb,cc)
            print("the product of a, b and c is: ",aa*bb*cc)  
   