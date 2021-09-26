'''Question 2
Write a function to calculate number e (base of natural logarithms 2.718281828459045...)
using formula '''
import math
def number_e(n):
    e=0
    k=1
    for k in range(k,n+1):
        e+= 1/math.factorial(k)
        k+=1
    return e
n=int(input('Введіть n: '))
print(number_e(n))
