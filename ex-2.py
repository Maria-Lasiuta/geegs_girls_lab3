n = int(input("Enter the integer number greater than 1: " ))
def divisorSum(n):
    sum = 0
    for i in range(1, n + 1):
        
        j = 1
        while j * j <= i:
            if i % j == 0:
                if i / j == j:
                    sum += j
                else:
                    sum += j + i / j
            j = j + 1
    return int(sum)
print( divisorSum(n))



