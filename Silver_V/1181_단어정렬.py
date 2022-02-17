n = int(input())

word = []
for _ in range(n) :
  word.append(input())
  
wordSet = list(set(word))

sortedWord = []
for i in wordSet :
  sortedWord.append((len(i), i))
  
result = sorted(sortedWord)

for wordLen, word in result :
  print(word)
