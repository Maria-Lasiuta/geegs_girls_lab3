#encryption function (first even indexes 0,2,4 ... then odd 1,3,5 ...)
def encrypt(strings):
    even = strings[::2] 
    odd = strings[1::2]
    print(even + odd)
message=input('Enter the message you want to encrypt: ')
encrypt(message)

#decryption function
def decrypt():
    string = input('Enter the message you want to decrypt : ')
    length = len(string)
    half_length = (length + 1) // 2 
    even=string[:half_length]
    odd=string[half_length:]
    x =  ''
    if length%2 == 0:
        for i in range (half_length):
            join=even[i] + odd[i]
            x = x + join
    else:
        for i in range (1,half_length + 1):
            start= i - 1
            join = even[start:i] + odd[start:i]
            x = x + join
    print(x)
decrypt()


