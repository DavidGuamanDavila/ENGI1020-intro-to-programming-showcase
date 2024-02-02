g = int(input('How many words do you wish to enter?'))

wordList = []
firstLetters = ""

for i in range(g): 
    
    a = input("Word?")
    
    wordList.append(a)
    
    longestWord = max(wordList, key=len)
    
    
print(wordList)
print(longestWord)



for i in wordList:
    
    firstLetters += i[0]
    
print(firstLetters)