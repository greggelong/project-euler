bignums = []

with open ('/home/gregk/Downloads/projectEuler/euler13/bignum.txt','r') as file:
    for line in file:
        bignums.append(int(line))
        

print(bignums)
print(sum(bignums))
