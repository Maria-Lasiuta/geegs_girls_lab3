#Find the key of the maximum value in a dictionary
dct = {'a': 15, 'b': 38, 'c': 76, 'd': 76, 'e': 76, 'f': 43}
m = [k for k,v in dct.items() if v == max(dct.values())]
print(m)
