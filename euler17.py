#one thousand //total:  21124



upto_nineteen = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
 
by_ten = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
 

totalLetters=0;

def countLetters(wrd):
    
    ## take out spaces
    wrdc = wrd.replace(" ","")
    ## take out hyphen
    wrdcc = wrdc.replace("-","")
    #print(wrd, wrdcc, len(wrdcc))
    return len(wrdcc)


def spellNumber(number):
    pass
    
    ## convert number to string to manipulate it
    nstr = str(number)
    ## initialize a string to hold result
    result = ""
    
    ## loop while nstr is not ""
    
    while nstr != "":
        
        ## check nstr length and perform transform
        
        if len(nstr) == 4:  #only one case for 1000
            result = "one thousand"
            nstr = "" # set nstr to "" so it breaks loop
            
        elif len(nstr) == 3:
            ## add word for number + hundred
            result = result + upto_nineteen[int(nstr[0])] + " hundred "
            ## take that number off nstr eg a="255", a=a[1:], a is "55"
            nstr = nstr[1:]
            ## check as see if the remainder is equal to zero if so no and
            ## break
            if int(nstr) == 0:
                break
            else:
                result = result + "and "
                
            
        ## now check >= 20  N.B. not checking len but value 
        elif int(nstr) >= 20:
            ## add 10s place
            result = result + by_ten[int(nstr[0])]
            ## take that number off nstr eg a="25", a=a[1:], a is "5"
            nstr = nstr[1:]
            ## check as see if the remainder is equal to zero if so no and
            ## break
            if int(nstr) == 0:
                break
            else:
                result = result + "-" 
            
        elif int(nstr) < 20:
            ## add zero to 19
            result = result + upto_nineteen[int(nstr)]
            nstr = "" # to break the loop
    return result
    
 

print(spellNumber(115))
print(countLetters(spellNumber(115)))

total =0

for i in range(1, 1001):
    a = spellNumber(i)
    total = total + countLetters(a)
    print(a, "//total: ",total)
