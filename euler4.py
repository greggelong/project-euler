def ispalind(n):
    nstr = str(n)
    rvnstr = nstr[::-1]
    rvn = int(rvnstr)
    return n == rvn

def threeDigitPalin():
    plist = []
    for i in range(100,1000):
        for j in range (100,1000):
            num = i*j
            
            if ispalind(num) and num not in plist:
                plist.append(num)
            
    return plist, max(plist)      
    

def threeDigitPalin2():
    plist = []
    i = 100
    while i <= 999:
        j=i
        while j <= 999:
            num = i*j
            #print(i,j, i*j)
            
            if ispalind(num) and num not in plist:
                plist.append(num)
            j+=1
        i+=1
    return plist, max(plist)      
    
print(ispalind(100))
mylist, maxie = threeDigitPalin2()
print(maxie)
print(mylist)
print(len(mylist))
