#Check if the number is prime
def is_prime(n):
     if n > 1:
         for i in range(2, (int(n/2)+1)):
             if n%i == 0:
                 return f'{n} is not a prime number'
             else:
                 return f'{n} is a prime nummber'
     else:
         return f'{n} is a prime number'
n = int(input('Enter integer number: '))
print(is_prime(n))
