alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for k in range(len(alphabet)):
    for j in range(len(alphabet)):
        print(alphabet[j-k],end='')
    print('\n')

