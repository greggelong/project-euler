"""
this one is odd it seems to have an odd history to as it was changed in 2014 from 5 to
13 adj numbers

 
I thought I wasnt checking well enough but I was
I am checking adjacent digets like moving a thirteen digit ruler over the entire
list.

I change the string to a list of ints with list comprehension

I have two solutions
one silly and one less silly

"""




a='7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'

b= [int(d) for d in str(a)]

print(b,len(b)/13)



# silly way

biggest =0
for num in range(12,len(b)-14):
    num1 = b[num]
    num2 = b[num+1]
    num3 = b[num+2]
    num4 = b[num+3]
    num5 = b[num+4]
    num6 = b[num+5]
    num7 = b[num+6]
    num8 = b[num+7]
    num9 = b[num+8]
    num10 = b[num+9]
    num11 = b[num+10]
    num12 = b[num+11]
    num13 = b[num+12]
     
    testbig = num1*num2*num3*num4*num5*num6*num7*num8*num9*num10*num11*num12*num13
    if testbig > biggest:
        biggest = testbig
        
print(biggest)

# a little better
biggest =0

for x in range(0,len(b)-13):
    testbig = 1  #for each number you must reset test big 
    for y in range(13):
        testbig = testbig * b[x+y]
        if testbig > biggest:
            biggest = testbig
        
print(biggest)