import math

#def answer(n):
#    # log base 2 (n) + 1
#    return int(math.ceil(math.log(n,2)))

def prime_factor(n):
    if n <= 1:
        return [1]
    for i in range(2, int(math.ceil(n/2))):
        if n % i == 0:
	    return prime_factor(n/i) + [i]
    return [1, n]

def answer(n):
    simple = 2*int(math.ceil(math.log(n,2)))
    complicated = [(n/x + answer(x)) for x in prime_factor(n) if x != n]
    return min([simple] + complicated)

print set(prime_factor(21)) == set([1, 3,7])  
print set(prime_factor(1)) == set([1])  
print set(prime_factor(15)) == set([1,3,5])  
print set(prime_factor(105)) == set([1,3,7,5])  

import pdb; pdb.set_trace()

print answer(1) == 0
print answer(2) == 2
print answer(3) == 3
print answer(4) == 4
print answer(5) == 5
print answer(6) == 5
print answer(7) == 6
print answer(8) == 6
print answer(9) == 6
print answer(10) == 7
print answer(12) == 7
print answer(11) == 8
print answer(15) == 8
print answer(16) == 8
print answer(21) == 9


#a
#aa 1 
#aaaa 2
#aaaaaaaaaaaa 3
