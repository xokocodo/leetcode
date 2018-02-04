





A = Solution()

print set(A.prime_factor(21)) == set([3,7])  
print set(A.prime_factor(1)) == set([])  
print set(A.prime_factor(15)) == set([3,5])  
print set(A.prime_factor(105)) == set([3,7,5])  

print A.minSteps(1) == 0
print A.minSteps(2) == 2
print A.minSteps(3) == 3
print A.minSteps(4) == 4
print A.minSteps(5) == 5
print A.minSteps(6) == 5
print A.minSteps(7) == 7
print A.minSteps(8) == 6
print A.minSteps(9) == 6
print A.minSteps(10) == 7
print A.minSteps(12) == 7
print A.minSteps(11) == 11
print A.minSteps(15) == 8
print A.minSteps(16) == 8
print A.minSteps(21) == 10