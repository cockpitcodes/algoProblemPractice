
givenString = 'ad<Wx'
# givenString = 'ab-cd'
# givenString = 'a-bC-dEf=ghIj!!'
emptyLetterList = []
nlDict = {}
emptyNLList = []

def callme(string):
    for st,_ in enumerate(string):
        if ((ord(string[st])>=65 and ord(string[st])<=90) or (ord(string[st])>=97 and ord(string[st])<=122)):
            emptyLetterList.append(string[st])
        else:
            nlDict[st] = string[st]

callme(givenString)
emptyLetterList.reverse()
newList = emptyLetterList
for i in nlDict:
    newList.insert(i, givenString[i])

print(''.join(newList))



# 1
# Input = 'ab-cd'
# Output = 'dc-ba'

# 2
# Input = 'a-bC-dEf=ghIj!!'
# Output = 'j-Ih-gfE=dCba!!'