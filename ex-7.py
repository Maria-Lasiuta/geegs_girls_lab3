text = open('text.txt', 'r')
numChars = 0
numWords = 0 
numLines = 0
for line in text:
    numLines += 1
    line = line.strip("\n")
    numChars += len(line)
    list1 = line.split()
    numWords += len(list1)
    
print("Number of characters: ", numChars)
print("Number of words: ", numWords)
print("Number of lines: ", numLines)
