# Вывести последнюю букву в слове
#word = 'Архангельск'
#print(word[-2])


# Вывести количество букв "а" в слове
#word = 'Архангельск'
#print(len(word))


# Вывести количество гласных букв в слове
#word = 'Архангельск'
#vocals=["а","е","ё","и","о","у","э","ю","я"]
#word = word.lower()
#a=0
#for letter in word:
#    if letter in vocals:
#        a += 1
#print(a)        


# Вывести количество слов в предложении
#sentence = 'Мы приехали в гости'
#a=0
#for word in sentence.split():
#    a +=1
#print(a)

# Вывести первую букву каждого слова на отдельной строке
#sentence = 'Мы приехали в гости'
#a=0
#b = sentence.split()
#for word in b:
#    print(word[0])



# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
b = sentence.split()
# b - список слов в выражении
dlw=0
b1 = len(b)
print(b1)
for word in b:
    dlw += len(word)
print(dlw)
print(dlw/b1)

