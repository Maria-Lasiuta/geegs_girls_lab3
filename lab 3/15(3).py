#reverse the dictionary
dct = {'a': 10, 'b': 11, 'c': 12, 'd': 9, 'e': 13}
dct = {v: k for k, v in dct.items()}
print(dct)
