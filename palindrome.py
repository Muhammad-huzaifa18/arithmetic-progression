print('Muhammad Huzaifa')
print('18b-048-CS')
print('Prgramming Ex#4')
word= str(input('Enter a word: '))
word_1=word.casefold()
reverseword= reversed(word)
if list (word)== list (reverseword):
    print('YES,Your word is a palindrome')
else:
    print('Sorry,Your word is not a palindrome')
