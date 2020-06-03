print('Please enter the first word or sentence')
word1 = input()
print('Typed characters:',word1)

print('Please enter the second word or sentence')
word2 = input()
print('Typed characters:',word2)

word1count = len(word1)
word2count = len(word2)

if word1count >= word2count:
 i = word1count
else:
 i = word2count

wordlist1 = list(word1)
wordlist2 = list(word2)
 
ans = ''
for x in range(100):
 if x == i-1:
  break
 w1 = wordlist1[x]
 w2 = wordlist2[x]
 if w1 == w2:
  ans += 'o'
 else:
  y = x
  if y+1 < i:
   y+=1
   w1 = wordlist1[y]
   if w1 == w2:
    wordlist2.insert(x,' ')
    i += 1
    ans += '×'
   else:
    w1 = wordlist1[x]
    w2 = wordlist2[y]
    if w1 == w2:
     wordlist1.insert(x,' ')
     i += 1
     ans += '×'
    else: 
     ans += '×'
  else:
   ans += '×'
answord1 = ''.join(wordlist1)
answord2 = ''.join(wordlist2)
print('answer')
print(answord1)
print(answord2)
print(ans)
