#Write a procedure which finds the Greatest Common Divisor of 2 numbers,
#which is defined as the largest number which will evenly divide two other numbers.

def divisor(a, b):
    d = 1
    for i in range(min(a,b), 1, -1):
        if a % i == 0 and b % i == 0:
            d = max(i, d)
    return d
a = int(input('Enter first number:'))
b = int(input('Enter second number:'))
print('the Greatest Common Divisor of a&b:', divisor(a, b))
