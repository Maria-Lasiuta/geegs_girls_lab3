#Calculate N! (factorial)

def factorial(n):
    if n<=0:
        return 1 #Numbers must be positive
    else:
        return n * factorial(n-1)
n = int(input('Enter a positive number:'))
print(factorial(n))
