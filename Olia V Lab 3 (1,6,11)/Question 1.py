'''Question 1
The Fibonacci numbers are the sequence below, where the first two numbers are 1,
and each number thereafter is the sum of the two preceding numbers. Write a
program that asks the user how many Fibonacci numbers to print and then prints
that many
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, …'''
count = int(input("How many fibonacci numbers would you like to print? "))
i = 1
if count == 0:
    fib = []
elif count == 1:
    fib = [1]
elif count == 2:
    fib = [1,1]
elif count > 2:
    fib = [1,1]
    while i < (count - 1):
        fib.append(fib[i] + fib[i-1])
        i += 1
print(f'The number of Fibonacci: ',fib)
