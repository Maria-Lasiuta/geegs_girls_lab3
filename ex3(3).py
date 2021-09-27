#Calculate number of distinct characters in a string using a for loop.
def unique_count(word):
  k=list()
  b = word.split()
  b = ''.join(b)
  for x in b:                   
    if x not in k:
      k.append(x)
  return len(k)
enter=input()
print('унікальних символів:',unique_count(enter))











        
        
